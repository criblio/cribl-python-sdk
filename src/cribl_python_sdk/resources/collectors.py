"""Collectors resource."""
from __future__ import annotations

from typing import Any, Literal

from .._response import SDKResponse
from ..models import Collector, PaginatedResponse, SavedJob
from ._base import BaseResource


class CollectorsResource(BaseResource):
    """Manage Collectors (scheduled data collection jobs)."""

    def list(
        self,
        *,
        collectorType: Literal["azure_blob", "cribl_lake", "database", "filesystem", "google_cloud_storage", "health_check", "rest", "s3", "script", "splunk"] | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[SavedJob]]:
        """List all Collectors.

        Get a list of all Collectors.

        Args:
            collectorType: Filter by collector type. Valid values: "azure_blob", "cribl_lake", "database", "filesystem", "google_cloud_storage", "health_check", "rest", "s3", "script", "splunk".
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing a list of SavedJob objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if collectorType is not None:
            params["collectorType"] = collectorType
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get("/lib/jobs", cast_to=PaginatedResponse[SavedJob], params=params or None)

    async def list_async(
        self,
        *,
        collectorType: Literal["azure_blob", "cribl_lake", "database", "filesystem", "google_cloud_storage", "health_check", "rest", "s3", "script", "splunk"] | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[SavedJob]]:
        """List all Collectors (async).

        Get a list of all Collectors.

        Args:
            collectorType: Filter by collector type. Valid values: "azure_blob", "cribl_lake", "database", "filesystem", "google_cloud_storage", "health_check", "rest", "s3", "script", "splunk".
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing a list of SavedJob objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if collectorType is not None:
            params["collectorType"] = collectorType
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return await self._get_async("/lib/jobs", cast_to=PaginatedResponse[SavedJob], params=params or None)

    def create(
        self,
        collector: Collector | dict[str, object],
    ) -> SDKResponse[PaginatedResponse[SavedJob]]:
        """Create a Collector.

        Create a new Collector.

        Args:
            collector: Full saved-job configuration as a typed Collector model
                (e.g. CollectorS3, CollectorScript) or a plain dict matching
                the ``POST /lib/jobs`` request body.

        Returns:
            (200) PaginatedResponse containing the created SavedJob.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = collector.model_dump(exclude_none=True) if hasattr(collector, "model_dump") else collector # pyright: ignore[reportAttributeAccessIssue]
        return self._post("/lib/jobs", cast_to=PaginatedResponse[SavedJob], json=body)

    async def create_async(
        self,
        collector: Collector | dict[str, object],
    ) -> SDKResponse[PaginatedResponse[SavedJob]]:
        """Create a Collector (async).

        Create a new Collector.

        Args:
            collector: Full saved-job configuration as a typed Collector model
                (e.g. CollectorS3, CollectorScript) or a plain dict matching
                the ``POST /lib/jobs`` request body.

        Returns:
            (200) PaginatedResponse containing the created SavedJob.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = collector.model_dump(exclude_none=True) if hasattr(collector, "model_dump") else collector # pyright: ignore[reportAttributeAccessIssue]
        return await self._post_async("/lib/jobs", cast_to=PaginatedResponse[SavedJob], json=body)

    def get(self, id: str) -> SDKResponse[PaginatedResponse[SavedJob]]:
        """Get a Collector.

        Get the specified Collector.

        Args:
            id: The `id` of the Collector to get.

        Returns:
            (200) PaginatedResponse containing the requested SavedJob.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(f"/lib/jobs/{id}", cast_to=PaginatedResponse[SavedJob])

    async def get_async(self, id: str) -> SDKResponse[PaginatedResponse[SavedJob]]:
        """Get a Collector (async).

        Get the specified Collector.

        Args:
            id: The `id` of the Collector to get.

        Returns:
            (200) PaginatedResponse containing the requested SavedJob.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"/lib/jobs/{id}", cast_to=PaginatedResponse[SavedJob])

    def update(
        self,
        id: str,
        collector: Collector | dict[str, object],
    ) -> SDKResponse[PaginatedResponse[SavedJob]]:
        """Update a Collector.

        Update the specified Collector. Provide a complete representation —
        this endpoint does not support partial updates; omitted fields are removed.

        Args:
            id: The `id` of the Collector to update.
            collector: Complete saved-job configuration as a typed model or dict.

        Returns:
            (200) PaginatedResponse containing the updated SavedJob.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = collector.model_dump(exclude_none=True) if hasattr(collector, "model_dump") else dict(collector) # pyright: ignore[reportAttributeAccessIssue]
        body["id"] = id
        return self._patch(f"/lib/jobs/{id}", cast_to=PaginatedResponse[SavedJob], json=body)

    async def update_async(
        self,
        id: str,
        collector: Collector | dict[str, object],
    ) -> SDKResponse[PaginatedResponse[SavedJob]]:
        """Update a Collector (async).

        Update the specified Collector. Provide a complete representation —
        this endpoint does not support partial updates; omitted fields are removed.

        Args:
            id: The `id` of the Collector to update.
            collector: Complete saved-job configuration as a typed model or dict.

        Returns:
            (200) PaginatedResponse containing the updated SavedJob.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = collector.model_dump(exclude_none=True) if hasattr(collector, "model_dump") else dict(collector) # pyright: ignore[reportAttributeAccessIssue]
        body["id"] = id
        return await self._patch_async(f"/lib/jobs/{id}", cast_to=PaginatedResponse[SavedJob], json=body)

    def delete(self, id: str) -> SDKResponse[PaginatedResponse[SavedJob]]:
        """Delete a Collector.

        Delete the specified Collector.

        Args:
            id: The `id` of the Collector to delete.

        Returns:
            (200) PaginatedResponse containing the deleted SavedJob.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._delete(f"/lib/jobs/{id}", cast_to=PaginatedResponse[SavedJob])

    async def delete_async(self, id: str) -> SDKResponse[PaginatedResponse[SavedJob]]:
        """Delete a Collector (async).

        Delete the specified Collector.

        Args:
            id: The `id` of the Collector to delete.

        Returns:
            (200) PaginatedResponse containing the deleted SavedJob.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._delete_async(f"/lib/jobs/{id}", cast_to=PaginatedResponse[SavedJob])
