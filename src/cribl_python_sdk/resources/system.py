"""System resource."""
from __future__ import annotations

from collections.abc import Generator, AsyncGenerator
from typing import TYPE_CHECKING, Any

from .._response import SDKResponse
from .._streaming import iter_ndjson, aiter_ndjson
from ..models import (
    ApiSettingsParam,
    AppsSettingsParam,
    BackupsSettingsParam,
    CapturedEvent,
    CustomLogoParam,
    PaginatedResponse,
    PiiSettingsParam,
    ProxySettingsParam,
    RollbackSettingsParam,
    ShutdownSettingsParam,
    SniSettingsParam,
    SocketsSettingsParam,
    SupportSettingsParam,
    SystemSettings,
    SystemSettingsSystemParam,
    TlsSettingsParam,
    UpgradeGroupSettingsParam,
    UpgradeSettingsParam,
    WorkersSettingsParam,
)
from ._base import BaseResource

if TYPE_CHECKING:
    from ..client import Cribl


class SystemCapturesResource(BaseResource):
    """Capture operations (`system.captures`)."""

    def _capture_body(
        self,
        *,
        duration: int | None = None,
        filter: str | None = None,
        level: int | None = None,
        maxEvents: int | None = None,
        stepDuration: int | None = None,
        workerId: str | None = None,
        workerThreshold: int | None = None,
    ) -> dict[str, Any]:
        body: dict[str, Any] = {}
        if duration is not None:
            body["duration"] = duration
        if filter is not None:
            body["filter"] = filter
        if level is not None:
            body["level"] = level
        if maxEvents is not None:
            body["maxEvents"] = maxEvents
        if stepDuration is not None:
            body["stepDuration"] = stepDuration
        if workerId is not None:
            body["workerId"] = workerId
        if workerThreshold is not None:
            body["workerThreshold"] = workerThreshold
        return body

    def create(
        self,
        *,
        duration: int | None = None,
        filter: str | None = None,
        level: int | None = None,
        maxEvents: int | None = None,
        stepDuration: int | None = None,
        workerId: str | None = None,
        workerThreshold: int | None = None,
    ) -> Generator[CapturedEvent, None, None]:
        """Capture live data as an NDJSON stream.

        Initiate a live data capture from Cribl Workers. Yields CapturedEvent
        objects as they arrive over the wire (line-delimited JSON).

        Args:
            duration: Amount of time to keep capture open, in seconds. If not provided, the default is 5 seconds.
            filter: JavaScript expression evaluated against each event to determine whether an event is included in the capture output. Expressions can reference any event field and use logical operators. If not provided, all events are captured.
            level: Stage at which events are captured. If not provided, the default is 0.
            maxEvents: Maximum number of events to capture. If not provided, the default is 100.
            stepDuration: How long to wait before increasing the capture sample size. Specify 1 second or longer. If not provided, the default is 5 seconds.
            workerId: Unique ID of the Worker.
            workerThreshold: Maximum number of Workers that can capture initially. A value of 0 means unlimited (all available Workers can capture). If not provided, the default is 50.

        Yields:
            (200) CapturedEvent objects parsed from NDJSON lines.

        Raises:
            ValidationError (400): Failed validation or malformed input — No worker nodes are connected to this worker group.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = self._capture_body(
            duration=duration, filter=filter, level=level, maxEvents=maxEvents,
            stepDuration=stepDuration, workerId=workerId, workerThreshold=workerThreshold,
        )
        self._client._ensure_token_valid()
        with self._client._client.stream("POST", "/system/capture", json=body) as resp:
            if resp.status_code >= 400:
                resp.read()
                from ..exceptions import APIError
                raise APIError.from_response(resp)
            yield from iter_ndjson(resp, CapturedEvent)

    async def create_async(
        self,
        *,
        duration: int | None = None,
        filter: str | None = None,
        level: int | None = None,
        maxEvents: int | None = None,
        stepDuration: int | None = None,
        workerId: str | None = None,
        workerThreshold: int | None = None,
    ) -> AsyncGenerator[CapturedEvent, None]:
        """Capture live data as an NDJSON stream (async).

        Initiate a live data capture from Cribl Workers. Yields CapturedEvent
        objects as they arrive over the wire (line-delimited JSON).

        Args:
            duration: Amount of time to keep capture open, in seconds. If not provided, the default is 5 seconds.
            filter: JavaScript expression evaluated against each event to determine whether an event is included in the capture output. Expressions can reference any event field and use logical operators. If not provided, all events are captured.
            level: Stage at which events are captured. If not provided, the default is 0.
            maxEvents: Maximum number of events to capture. If not provided, the default is 100.
            stepDuration: How long to wait before increasing the capture sample size. Specify 1 second or longer. If not provided, the default is 5 seconds.
            workerId: Unique ID of the Worker.
            workerThreshold: Maximum number of Workers that can capture initially. A value of 0 means unlimited (all available Workers can capture). If not provided, the default is 50.

        Yields:
            (200) CapturedEvent objects parsed from NDJSON lines.

        Raises:
            ValidationError (400): Failed validation or malformed input — No worker nodes are connected to this worker group.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = self._capture_body(
            duration=duration, filter=filter, level=level, maxEvents=maxEvents,
            stepDuration=stepDuration, workerId=workerId, workerThreshold=workerThreshold,
        )
        self._client._ensure_token_valid()
        async with self._client._async_client.stream("POST", "/system/capture", json=body) as resp:
            if resp.status_code >= 400:
                await resp.aread()
                from ..exceptions import APIError
                raise APIError.from_response(resp)
            async for event in aiter_ndjson(resp, CapturedEvent):
                yield event


class SystemSettingsCriblResource(BaseResource):
    """Cribl settings operations (`system.settings.cribl`)."""

    def list(self) -> SDKResponse[PaginatedResponse[SystemSettings]]:
        """Get system settings.

        Get the current Cribl system settings.

        Returns:
            (200) PaginatedResponse containing the requested SystemSettings.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get("/system/settings/conf", cast_to=PaginatedResponse[SystemSettings])

    async def list_async(self) -> SDKResponse[PaginatedResponse[SystemSettings]]:
        """Get system settings (async).

        Get the current Cribl system settings.

        Returns:
            (200) PaginatedResponse containing the requested SystemSettings.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async("/system/settings/conf", cast_to=PaginatedResponse[SystemSettings])

    def update(
        self,
        *,
        api: ApiSettingsParam | None = None,
        apps: AppsSettingsParam | None = None,
        backups: BackupsSettingsParam | None = None,
        customLogo: CustomLogoParam | None = None,
        pii: PiiSettingsParam | None = None,
        proxy: ProxySettingsParam | None = None,
        rollback: RollbackSettingsParam | None = None,
        shutdown: ShutdownSettingsParam | None = None,
        sni: SniSettingsParam | None = None,
        sockets: SocketsSettingsParam | None = None,
        support: SupportSettingsParam | None = None,
        system: SystemSettingsSystemParam | None = None,
        tls: TlsSettingsParam | None = None,
        upgradeGroupSettings: UpgradeGroupSettingsParam | None = None,
        upgradeSettings: UpgradeSettingsParam | None = None,
        workers: WorkersSettingsParam | None = None,
    ) -> SDKResponse[PaginatedResponse[SystemSettings]]:
        """Update system settings.

        Update the specified Cribl system settings.

        Provide only the top-level sections (`api`, `workers`, `tls`, `proxy`,
        etc.) you want to change. Omitted sections stay unchanged. Each provided
        section fully replaces the existing one -- send the complete section
        object, not only the changed fields.

        Args:
            api: API server configuration for the Cribl instance.
            apps: App configuration.
            backups: Configuration backup settings, including storage location and retention period.
            customLogo: Custom logo configuration for the Cribl UI login page and navigation bar.
            pii: Personally identifiable information (PII) detection configuration.
            proxy: HTTP proxy configuration for outbound connections.
            rollback: Automatic rollback settings applied when an upgrade fails.
            shutdown: Graceful shutdown configuration.
            sni: Server Name Indication (SNI) routing configuration.
            sockets: Unix domain socket configuration.
            support: Support and diagnostics settings.
            system: System-level operational settings for the Cribl instance.
            tls: Global TLS/SSL settings applied to all outbound connections that do not specify their own TLS configuration.
            upgradeGroupSettings: Rolling upgrade group settings that control how many nodes are upgraded at a time.
            upgradeSettings: Automatic upgrade scheduling and package source configuration.
            workers: Worker Process configuration.

        Returns:
            (200) PaginatedResponse containing the updated SystemSettings.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized to perform this action.
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {}
        if api is not None:
            body["api"] = api
        if apps is not None:
            body["apps"] = apps
        if backups is not None:
            body["backups"] = backups
        if customLogo is not None:
            body["customLogo"] = customLogo
        if pii is not None:
            body["pii"] = pii
        if proxy is not None:
            body["proxy"] = proxy
        if rollback is not None:
            body["rollback"] = rollback
        if shutdown is not None:
            body["shutdown"] = shutdown
        if sni is not None:
            body["sni"] = sni
        if sockets is not None:
            body["sockets"] = sockets
        if support is not None:
            body["support"] = support
        if system is not None:
            body["system"] = system
        if tls is not None:
            body["tls"] = tls
        if upgradeGroupSettings is not None:
            body["upgradeGroupSettings"] = upgradeGroupSettings
        if upgradeSettings is not None:
            body["upgradeSettings"] = upgradeSettings
        if workers is not None:
            body["workers"] = workers
        return self._patch("/system/settings/conf", cast_to=PaginatedResponse[SystemSettings], json=body)

    async def update_async(
        self,
        *,
        api: ApiSettingsParam | None = None,
        apps: AppsSettingsParam | None = None,
        backups: BackupsSettingsParam | None = None,
        customLogo: CustomLogoParam | None = None,
        pii: PiiSettingsParam | None = None,
        proxy: ProxySettingsParam | None = None,
        rollback: RollbackSettingsParam | None = None,
        shutdown: ShutdownSettingsParam | None = None,
        sni: SniSettingsParam | None = None,
        sockets: SocketsSettingsParam | None = None,
        support: SupportSettingsParam | None = None,
        system: SystemSettingsSystemParam | None = None,
        tls: TlsSettingsParam | None = None,
        upgradeGroupSettings: UpgradeGroupSettingsParam | None = None,
        upgradeSettings: UpgradeSettingsParam | None = None,
        workers: WorkersSettingsParam | None = None,
    ) -> SDKResponse[PaginatedResponse[SystemSettings]]:
        """Update system settings (async).

        Update the specified Cribl system settings.

        Provide only the top-level sections (`api`, `workers`, `tls`, `proxy`,
        etc.) you want to change. Omitted sections stay unchanged. Each provided
        section fully replaces the existing one -- send the complete section
        object, not only the changed fields.

        Args:
            api: API server configuration for the Cribl instance.
            apps: App configuration.
            backups: Configuration backup settings, including storage location and retention period.
            customLogo: Custom logo configuration for the Cribl UI login page and navigation bar.
            pii: Personally identifiable information (PII) detection configuration.
            proxy: HTTP proxy configuration for outbound connections.
            rollback: Automatic rollback settings applied when an upgrade fails.
            shutdown: Graceful shutdown configuration.
            sni: Server Name Indication (SNI) routing configuration.
            sockets: Unix domain socket configuration.
            support: Support and diagnostics settings.
            system: System-level operational settings for the Cribl instance.
            tls: Global TLS/SSL settings applied to all outbound connections that do not specify their own TLS configuration.
            upgradeGroupSettings: Rolling upgrade group settings that control how many nodes are upgraded at a time.
            upgradeSettings: Automatic upgrade scheduling and package source configuration.
            workers: Worker Process configuration.

        Returns:
            (200) PaginatedResponse containing the updated SystemSettings.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized to perform this action.
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {}
        if api is not None:
            body["api"] = api
        if apps is not None:
            body["apps"] = apps
        if backups is not None:
            body["backups"] = backups
        if customLogo is not None:
            body["customLogo"] = customLogo
        if pii is not None:
            body["pii"] = pii
        if proxy is not None:
            body["proxy"] = proxy
        if rollback is not None:
            body["rollback"] = rollback
        if shutdown is not None:
            body["shutdown"] = shutdown
        if sni is not None:
            body["sni"] = sni
        if sockets is not None:
            body["sockets"] = sockets
        if support is not None:
            body["support"] = support
        if system is not None:
            body["system"] = system
        if tls is not None:
            body["tls"] = tls
        if upgradeGroupSettings is not None:
            body["upgradeGroupSettings"] = upgradeGroupSettings
        if upgradeSettings is not None:
            body["upgradeSettings"] = upgradeSettings
        if workers is not None:
            body["workers"] = workers
        return await self._patch_async("/system/settings/conf", cast_to=PaginatedResponse[SystemSettings], json=body)


class SystemSettingsResource(BaseResource):
    """Settings operations (`system.settings`)."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.cribl = SystemSettingsCriblResource(client)

    def restart(self) -> SDKResponse[bool]:
        """Restart the Cribl server.

        This operation requires `system.restart` to be set to `api` in
        `cribl.yml`. If this setting is not configured, the request returns a
        `403` error.

        Restarting the server causes a brief period of downtime while the
        process stops and restarts. All in-flight events are drained before the
        process exits. Use `POST /system/settings/reload` to apply configuration
        changes without a full restart.

        Returns:
            (200) bool indicating restart was initiated.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Restart from the API is disabled. Set system.restart to api in cribl.yml to enable it.
            ServerError (500): Unexpected server error.
        """
        resp = self._client._request("POST", "/system/settings/restart")
        data = resp.json() if resp.content else {}
        items = data.get("items", [{}])
        restarted = bool(items[0].get("restarted", False)) if items and isinstance(items[0], dict) else True
        return SDKResponse(data=restarted, status_code=resp.status_code, headers=resp.headers, raw_response=resp)

    async def restart_async(self) -> SDKResponse[bool]:
        """Restart the Cribl server (async).

        This operation requires `system.restart` to be set to `api` in
        `cribl.yml`. If this setting is not configured, the request returns a
        `403` error.

        Restarting the server causes a brief period of downtime while the
        process stops and restarts. All in-flight events are drained before the
        process exits. Use `POST /system/settings/reload` to apply configuration
        changes without a full restart.

        Returns:
            (200) bool indicating restart was initiated.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Restart from the API is disabled. Set system.restart to api in cribl.yml to enable it.
            ServerError (500): Unexpected server error.
        """
        resp = await self._client._request_async("POST", "/system/settings/restart")
        data = resp.json() if resp.content else {}
        items = data.get("items", [{}])
        restarted = bool(items[0].get("restarted", False)) if items and isinstance(items[0], dict) else True
        return SDKResponse(data=restarted, status_code=resp.status_code, headers=resp.headers, raw_response=resp)


class SystemResource(BaseResource):
    """System settings, restart, and event capture."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.captures = SystemCapturesResource(client)
        self.settings = SystemSettingsResource(client)
