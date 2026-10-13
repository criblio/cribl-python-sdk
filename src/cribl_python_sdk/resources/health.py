"""Health check resource."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from pydantic import TypeAdapter

from .._response import SDKResponse
from ..models import HealthServerStatus, WorkerHealthStatus
from ._base import BaseResource

if TYPE_CHECKING:
    from ..client import Cribl

_WORKER_HEALTH_STATUS_ADAPTER: TypeAdapter[WorkerHealthStatus] = TypeAdapter(WorkerHealthStatus)


class HealthWorkersResource(BaseResource):
    """Health status of Worker Processes (`health.workers`)."""

    def get(self, *, scope: Literal["default", "all"] | None = None) -> SDKResponse[WorkerHealthStatus]:
        """Get the health status of Worker Processes.

        Get the current health status of Worker Processes that the server manages.

        Args:
            scope: Which Worker Processes to report on. `default` reflects only the
                primary Worker Process (`w:0`). `all` requires every Worker Process
                — plus the Load Balancing Worker Process when it exists — to be
                fully booted, and returns per-process counts. Valid values: "default", "all".

        Returns:
            (200) WorkerHealthStatus: healthy (all up) or mixed (some up) status.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if scope is not None:
            params["scope"] = scope
        return self._get("/health/workers", cast_to=_WORKER_HEALTH_STATUS_ADAPTER, params=params or None)

    async def get_async(self, *, scope: Literal["default", "all"] | None = None) -> SDKResponse[WorkerHealthStatus]:
        """Get the health status of Worker Processes (async).

        Get the current health status of Worker Processes that the server manages.

        Args:
            scope: Which Worker Processes to report on. `default` reflects only the
                primary Worker Process (`w:0`). `all` requires every Worker Process
                — plus the Load Balancing Worker Process when it exists — to be
                fully booted, and returns per-process counts. Valid values: "default", "all".

        Returns:
            (200) WorkerHealthStatus: healthy (all up) or mixed (some up) status.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if scope is not None:
            params["scope"] = scope
        return await self._get_async("/health/workers", cast_to=_WORKER_HEALTH_STATUS_ADAPTER, params=params or None)


class HealthResource(BaseResource):
    """Server health status."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.workers = HealthWorkersResource(client)

    def get(self) -> SDKResponse[HealthServerStatus]:
        """Get the health status of the application.

        Get the current health status of the server (Leader or Worker Node). In
        Distributed deployments, requests routed to a Worker or Edge node using
        the host context require a Bearer token for authentication.

        Returns:
            (200) HealthServerStatus with server health information.

        Raises:
            ServerError (500): Unexpected server error.
        """
        return self._get("/health", cast_to=HealthServerStatus)

    async def get_async(self) -> SDKResponse[HealthServerStatus]:
        """Get the health status of the application (async).

        Get the current health status of the server (Leader or Worker Node). In
        Distributed deployments, requests routed to a Worker or Edge node using
        the host context require a Bearer token for authentication.

        Returns:
            (200) HealthServerStatus with server health information.

        Raises:
            ServerError (500): Unexpected server error.
        """
        return await self._get_async("/health", cast_to=HealthServerStatus)
