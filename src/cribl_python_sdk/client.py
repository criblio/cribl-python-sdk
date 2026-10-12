"""Cribl Control Plane SDK client — unified sync + async."""
from __future__ import annotations

import atexit
import asyncio
import copy
import logging
import math
import os
import time
import weakref
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any, Literal, Self, TYPE_CHECKING

import httpx

from . import __gen_version__, __openapi_doc_version__, __version__
from ._retry import RetryConfig
from .exceptions import APIError, RateLimitError, ServerError
from .models import Security

if TYPE_CHECKING:
    from .resources.auth import AuthResource
    from .resources.cloud import CloudResource
    from .resources.collectors import CollectorsResource
    from .resources.database_connections import DatabaseConnectionsResource
    from .resources.datasets import DatasetsResource
    from .resources.destinations import DestinationsResource
    from .resources.functions import FunctionsResource
    from .resources.groups import GroupsResource
    from .resources.health import HealthResource
    from .resources.nodes import NodesResource
    from .resources.packs import PacksResource
    from .resources.pipelines import PipelinesResource
    from .resources.routes import RoutesResource
    from .resources.sources import SourcesResource
    from .resources.system import SystemResource
    from .resources.versioning import VersioningResource

logger = logging.getLogger("cribl_python_sdk")

MAX_RETRY_WAIT = 180.0
"""Upper bound (seconds) on a server-supplied retry delay, matching Cribl's own Retry-After ceiling."""


def _parse_retry_after(headers: httpx.Headers) -> float | None:
    """Seconds to wait per retry-after-ms or Retry-After, or None if absent/unparseable."""
    ms = headers.get("retry-after-ms")
    if ms is not None:
        try:
            millis = float(ms)
        except ValueError:
            return None
        return millis / 1000.0 if math.isfinite(millis) else None
    value = headers.get("retry-after")
    if value is None:
        return None
    try:
        seconds = float(value)
    except ValueError:
        # HTTP-date form (RFC 9110); parsedate_to_datetime covers the three legal date formats.
        try:
            when = parsedate_to_datetime(value)
        except (TypeError, ValueError):
            return None
        if when.tzinfo is None:
            when = when.replace(tzinfo=timezone.utc)
        return (when - datetime.now(timezone.utc)).total_seconds()
    return seconds if math.isfinite(seconds) else None


class Cribl:
    """Cribl Control Plane and Cribl.Cloud platform SDK client.

    Provides both sync and async methods on a single instance.
    Pass the control-plane origin only — the SDK appends /api/v1 internally.
    Platform (`cloud.*`) calls use the Cribl.Cloud gateway (default
    https://gateway.cribl.cloud) and spec paths as-is.

    Args:
        server_url: Control-plane origin (e.g. "http://localhost:9000" or your Cloud workspace URL).
        security: Authentication config (bearer token or OAuth2 credentials). Shared with cloud.* calls.
        cloud_server_url: Cribl.Cloud gateway origin. Default: https://gateway.cribl.cloud.
        timeout: Request timeout in seconds.
        debug: Enable debug logging (requests, responses, headers).

    Usage:
        >>> cribl = Cribl(server_url="http://localhost:9000",
        ...     security=Security(bearer_auth="token"))
        >>> pipelines = cribl.pipelines.list()
        >>> workspaces = cribl.cloud.workspaces.list("org-id")
    """

    API_BASE_PATH = "/api/v1"
    DEFAULT_CLOUD_SERVER_URL = "https://gateway.cribl.cloud"

    auth: AuthResource
    cloud: CloudResource
    collectors: CollectorsResource
    database_connections: DatabaseConnectionsResource
    datasets: DatasetsResource
    destinations: DestinationsResource
    functions: FunctionsResource
    groups: GroupsResource
    health: HealthResource
    nodes: NodesResource
    packs: PacksResource
    pipelines: PipelinesResource
    routes: RoutesResource
    sources: SourcesResource
    system: SystemResource
    versioning: VersioningResource

    def __init__(
        self,
        server_url: str,
        *,
        security: Security | None = None,
        cloud_server_url: str | None = None,
        timeout: float = 30.0,
        retry_config: RetryConfig | None = None,
        debug: bool = False,
        debug_logger: logging.Logger | None = None,
        hooks: list[Any] | None = None,
        http2: bool = False,
        http_client: httpx.Client | None = None,
        async_http_client: httpx.AsyncClient | None = None,
    ):
        """Initialize the Cribl Control Plane client.

        Args:
            server_url: Base URL of the Cribl instance (origin only, e.g. "http://localhost:9000"). SDK appends /api/v1.
            security: Authentication configuration. Use Security(username=, password=) for on-prem or Security(client_id=, client_secret=) for cloud. Shared with cloud.* (gateway) calls.
            cloud_server_url: Cribl.Cloud platform gateway origin. Default: https://gateway.cribl.cloud from openapi/management-plane.yml.
            timeout: HTTP request timeout in seconds. Default: 30.0.
            retry_config: Default retry configuration for all requests. Override per-operation by passing retry_config to resource methods. Default: RetryConfig().
            debug: Enable debug logging on SDK, httpx, and httpcore loggers. Default: False.
            debug_logger: Custom logger instance for SDK debug output. Overrides the default 'cribl_python_sdk' logger.
            hooks: List of hook objects with optional on_before_request(method, path, kwargs) and on_after_response(response) methods.
            http2: Enable HTTP/2 for connection multiplexing. Requires `httpx[http2]` (h2 package). Default: False.
            http_client: Custom httpx.Client for advanced use (proxies, mTLS, hooks). Overrides default client.
            async_http_client: Custom httpx.AsyncClient for advanced use. Overrides default async client.
        """
        self._server_url = server_url.rstrip("/")
        self._cloud_server_url = (cloud_server_url or self.DEFAULT_CLOUD_SERVER_URL).rstrip("/")
        self._security = security
        self._timeout = timeout
        self._retry_config = retry_config or RetryConfig()
        self._scope_path = ""
        self._debug = debug
        self._http2 = http2
        self._hooks = hooks or []
        self._custom_client = http_client
        self._custom_async_client = async_http_client
        should_debug = debug or os.environ.get("CRIBL_SDK_DEBUG", "").lower() in ("1", "true", "yes")
        if debug_logger:
            global logger
            logger = debug_logger
            logger.setLevel(logging.DEBUG)
        if should_debug:
            logger.setLevel(logging.DEBUG)
            logging.getLogger("httpx").setLevel(logging.DEBUG)
            logging.getLogger("httpcore").setLevel(logging.DEBUG)
        self._init_clients()
        self._init_auth()
        self._init_resources()
        self._prevent_leak()

    def _init_clients(self) -> None:
        base_url = f"{self._server_url}{self.API_BASE_PATH}{self._scope_path}"
        headers: dict[str, str] = {
            "Accept": "application/json",
            "User-Agent": f"cribl-python-sdk/python {__version__} {__gen_version__} {__openapi_doc_version__} cribl-control-plane",
        }
        if self._custom_client is not None:
            self._client = self._custom_client
        else:
            self._client = httpx.Client(base_url=base_url, headers=headers, timeout=self._timeout, http2=self._http2)
        if self._custom_async_client is not None:
            self._async_client = self._custom_async_client
        else:
            self._async_client = httpx.AsyncClient(base_url=base_url, headers=headers, timeout=self._timeout, http2=self._http2)
        cloud_headers = dict(headers)
        self._cloud_client = httpx.Client(
            base_url=self._cloud_server_url,
            headers=cloud_headers,
            timeout=self._timeout,
            http2=self._http2,
        )
        self._cloud_async_client = httpx.AsyncClient(
            base_url=self._cloud_server_url,
            headers=cloud_headers,
            timeout=self._timeout,
            http2=self._http2,
        )

    def _init_auth(self) -> None:
        if self._security is None:
            return
        if self._security.bearer_auth:
            self._set_bearer(self._security.bearer_auth)
        elif self._security.client_id and self._security.client_secret:
            self._refresh_oauth_token()
        elif self._security.username and self._security.password:
            self._login_with_credentials()

    def _refresh_oauth_token(self) -> None:
        """Fetch/refresh OAuth2 token using client credentials grant."""
        assert self._security is not None
        token_url = self._security.token_url or Security.CLOUD_TOKEN_URL
        audience = self._security.audience or Security.CLOUD_AUDIENCE
        try:
            resp = httpx.post(
                token_url,
                data={
                    "grant_type": "client_credentials",
                    "client_id": self._security.client_id,
                    "client_secret": self._security.client_secret,
                    "audience": audience,
                },
            )
        except httpx.ConnectError as exc:
            from .exceptions import ConnectionError
            raise ConnectionError(token_url, exc) from exc
        resp.raise_for_status()
        data = resp.json()
        self._oauth_token = data["access_token"]
        self._oauth_expires_at = time.time() + data.get("expires_in", 3600) - 60
        self._set_bearer(self._oauth_token)

    def _login_with_credentials(self) -> None:
        """Authenticate via POST /auth/login and set the JWT token with auto-refresh."""
        assert self._security is not None
        url = f"{self._server_url}{self.API_BASE_PATH}/auth/login"
        try:
            resp = httpx.post(
                url,
                json={"username": self._security.username, "password": self._security.password},
            )
        except httpx.ConnectError as exc:
            from .exceptions import ConnectionError
            raise ConnectionError(self._server_url, exc) from exc
        resp.raise_for_status()
        data = resp.json()
        token = data["token"]
        self._set_bearer(token)
        # Parse JWT exp claim for refresh timing (60s buffer)
        import base64, json as _json
        try:
            payload = token.split(".")[1]
            payload += "=" * (-len(payload) % 4)
            claims = _json.loads(base64.urlsafe_b64decode(payload))
            self._oauth_expires_at = claims["exp"] - 60
        except (IndexError, KeyError, ValueError):
            # Fallback: refresh in 1 hour
            self._oauth_expires_at = time.time() + 3600 - 60

    def _set_bearer(self, token: str) -> None:
        value = f"Bearer {token}"
        self._client.headers["Authorization"] = value
        self._async_client.headers["Authorization"] = value
        self._cloud_client.headers["Authorization"] = value
        self._cloud_async_client.headers["Authorization"] = value

    def _ensure_token_valid(self) -> None:
        """Refresh token if expired (OAuth2 or username/password)."""
        if not hasattr(self, "_oauth_expires_at") or time.time() < self._oauth_expires_at:
            return
        if self._security and self._security.client_id and self._security.client_secret:
            self._refresh_oauth_token()
        elif self._security and self._security.username and self._security.password:
            self._login_with_credentials()

    def _init_resources(self) -> None:
        from .resources.auth import AuthResource
        from .resources.cloud import CloudResource
        from .resources.collectors import CollectorsResource
        from .resources.database_connections import DatabaseConnectionsResource
        from .resources.datasets import DatasetsResource
        from .resources.destinations import DestinationsResource
        from .resources.functions import FunctionsResource
        from .resources.groups import GroupsResource
        from .resources.health import HealthResource
        from .resources.nodes import NodesResource
        from .resources.packs import PacksResource
        from .resources.pipelines import PipelinesResource
        from .resources.routes import RoutesResource
        from .resources.sources import SourcesResource
        from .resources.system import SystemResource
        from .resources.versioning import VersioningResource

        self.auth = AuthResource(self)
        self.cloud = CloudResource(self)
        self.collectors = CollectorsResource(self)
        self.database_connections = DatabaseConnectionsResource(self)
        self.datasets = DatasetsResource(self)
        self.destinations = DestinationsResource(self)
        self.functions = FunctionsResource(self)
        self.groups = GroupsResource(self)
        self.health = HealthResource(self)
        self.nodes = NodesResource(self)
        self.packs = PacksResource(self)
        self.pipelines = PipelinesResource(self)
        self.routes = RoutesResource(self)
        self.sources = SourcesResource(self)
        self.system = SystemResource(self)
        self.versioning = VersioningResource(self)

    def in_context(self, *, group_id: str | None = None, node_id: str | None = None) -> Self:
        """Return a scoped client routing to a worker group or node context.

        The scoped client shares auth but prefixes paths with /m/{group_id} or /w/{node_id}.
        """
        if not group_id and not node_id:
            raise ValueError("Provide group_id or node_id")
        # Shallow copy keeps config in sync with __init__; clients, auth and resources are rebuilt below.
        scoped = copy.copy(self)
        scoped._custom_client = None
        scoped._custom_async_client = None
        scoped._scope_path = f"/m/{group_id}" if group_id else f"/w/{node_id}"
        scoped._init_clients()
        scoped._init_auth()
        scoped._init_resources()
        return scoped

    def set_token(self, token: str) -> None:
        """Update the bearer token on both sync and async clients."""
        self._set_bearer(token)

    def _get_retry_wait(self, resp: httpx.Response, attempt: int, cfg: RetryConfig | None = None) -> float:
        """Parse Retry-After or retry-after-ms headers, fallback to exponential backoff.

        Malformed headers fall back to backoff; the result is clamped to [0, MAX_RETRY_WAIT].
        """
        wait = _parse_retry_after(resp.headers)
        if wait is None:
            factor = cfg.backoff_factor if cfg else 2.0
            wait = factor ** attempt
        return min(max(wait, 0.0), MAX_RETRY_WAIT)

    def _request(
        self,
        method: str,
        path: str,
        *,
        retry_config: RetryConfig | None = None,
        surface: Literal["control_plane", "cloud"] = "control_plane",
        **kwargs: Any,
    ) -> httpx.Response:
        """Execute a sync HTTP request with retry on configured status codes. Returns the raw httpx.Response."""
        self._ensure_token_valid()
        cfg = retry_config or self._retry_config
        retryable = cfg.retryable_statuses(method)
        http = self._cloud_client if surface == "cloud" else self._client
        for attempt in range(cfg.max_attempts):
            logger.debug("%s %s (attempt %d)", method, path, attempt + 1)
            self._run_hooks_before(method, path, kwargs)
            try:
                resp = http.request(method, path, **kwargs)
            except httpx.TimeoutException as exc:
                from .exceptions import TimeoutError
                raise TimeoutError(method, path, self._timeout, exc) from exc
            logger.debug("Response: %d %s", resp.status_code, resp.reason_phrase)
            self._run_hooks_after(resp)
            if resp.status_code in retryable and attempt < cfg.max_attempts - 1:
                time.sleep(self._get_retry_wait(resp, attempt, cfg))
                continue
            if resp.status_code == 429:
                raise RateLimitError(429, "Rate limit exceeded", resp)
            if resp.status_code >= 400:
                raise APIError.from_response(resp)
            return resp
        raise ServerError(resp.status_code, "All retries exhausted", resp)  # pyright: ignore[reportPossiblyUnboundVariable]

    async def _request_async(
        self,
        method: str,
        path: str,
        *,
        retry_config: RetryConfig | None = None,
        surface: Literal["control_plane", "cloud"] = "control_plane",
        **kwargs: Any,
    ) -> httpx.Response:
        """Execute an async HTTP request with retry on configured status codes. Returns the raw httpx.Response."""
        self._ensure_token_valid()
        cfg = retry_config or self._retry_config
        retryable = cfg.retryable_statuses(method)
        http = self._cloud_async_client if surface == "cloud" else self._async_client
        for attempt in range(cfg.max_attempts):
            logger.debug("%s %s (attempt %d)", method, path, attempt + 1)
            self._run_hooks_before(method, path, kwargs)
            try:
                resp = await http.request(method, path, **kwargs)
            except httpx.TimeoutException as exc:
                from .exceptions import TimeoutError
                raise TimeoutError(method, path, self._timeout, exc) from exc
            logger.debug("Response: %d %s", resp.status_code, resp.reason_phrase)
            self._run_hooks_after(resp)
            if resp.status_code in retryable and attempt < cfg.max_attempts - 1:
                await asyncio.sleep(self._get_retry_wait(resp, attempt, cfg))
                continue
            if resp.status_code == 429:
                raise RateLimitError(429, "Rate limit exceeded", resp)
            if resp.status_code >= 400:
                raise APIError.from_response(resp)
            return resp
        raise ServerError(resp.status_code, "All retries exhausted", resp)  # pyright: ignore[reportPossiblyUnboundVariable]

    def _run_hooks_before(self, method: str, path: str, kwargs: dict[str, Any]) -> None:
        for hook in self._hooks:
            if hasattr(hook, "on_before_request"):
                hook.on_before_request(method, path, kwargs)

    def _run_hooks_after(self, response: httpx.Response) -> None:
        for hook in self._hooks:
            if hasattr(hook, "on_after_response"):
                hook.on_after_response(response)

    def _prevent_leak(self) -> None:
        ref = weakref.ref(self)
        def _cleanup() -> None:
            obj = ref()
            if obj is not None:
                obj._client.close()
                obj._cloud_client.close()
        atexit.register(_cleanup)

    def close(self) -> None:
        """Close both sync and async HTTP clients."""
        self._client.close()
        self._cloud_client.close()

    async def close_async(self) -> None:
        """Close the async HTTP client."""
        await self._async_client.aclose()
        await self._cloud_async_client.aclose()

    def __repr__(self) -> str:
        auth = "none"
        if self._security:
            if self._security.bearer_auth:
                t = self._security.bearer_auth
                auth = f"bearer={t[:8]}****" if len(t) > 12 else "bearer=****"
            elif self._security.client_id:
                auth = f"oauth2(client_id={self._security.client_id[:8]}...)"
            elif self._security.username:
                auth = f"login(user={self._security.username})"
        return f"Cribl(server_url={self._server_url!r}, auth={auth})"

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.close_async()
