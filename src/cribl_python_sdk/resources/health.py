"""Health check resource."""
from __future__ import annotations

from .._response import SDKResponse
from ..models import HealthServerStatus
from ._base import BaseResource


class HealthResource(BaseResource):
    """Server health status."""

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
