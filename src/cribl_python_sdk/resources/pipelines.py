"""Pipelines resource."""
from __future__ import annotations

from typing import Any

from .._response import SDKResponse

from ..models import PaginatedResponse, Pipeline, PipelineConfParam
from ._base import BaseResource


class PipelinesResource(BaseResource):
    """Manage processing pipelines (create, list, update, delete)."""

    def _base(self, pack: str | None) -> str:
        return f"/p/{pack}/pipelines" if pack else "/pipelines"

    def list(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[Pipeline]]:
        """List all Pipelines.

        Get a list of all Pipelines.

        Args:
            offset: Pagination offset
            limit: Maximum number of items to return
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing a list of Pipeline objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get(self._base(pack), cast_to=PaginatedResponse[Pipeline], params=params or None)

    async def list_async(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[Pipeline]]:
        """List all Pipelines (async).

        Get a list of all Pipelines.

        Args:
            offset: Pagination offset
            limit: Maximum number of items to return
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing a list of Pipeline objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return await self._get_async(self._base(pack), cast_to=PaginatedResponse[Pipeline], params=params or None)

    def create(
        self,
        *,
        id: str,
        conf: PipelineConfParam,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[Pipeline]]:
        """Create a Pipeline.

        Create a new Pipeline.

        Args:
            id: Unique identifier for the Pipeline.
            conf: Configuration for the Pipeline, including functions and settings.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the created Pipeline.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id, "conf": conf}
        return self._post(self._base(pack), cast_to=PaginatedResponse[Pipeline], json=body)

    async def create_async(
        self,
        *,
        id: str,
        conf: PipelineConfParam,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[Pipeline]]:
        """Create a Pipeline (async).

        Create a new Pipeline.

        Args:
            id: Unique identifier for the Pipeline.
            conf: Configuration for the Pipeline, including functions and settings.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the created Pipeline.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id, "conf": conf}
        return await self._post_async(self._base(pack), cast_to=PaginatedResponse[Pipeline], json=body)

    def get(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[Pipeline]]:
        """Get a Pipeline.

        Get the specified Pipeline.

        Args:
            id: The `id` of the Pipeline to get.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested Pipeline.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[Pipeline])

    async def get_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[Pipeline]]:
        """Get a Pipeline (async).

        Get the specified Pipeline.

        Args:
            id: The `id` of the Pipeline to get.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested Pipeline.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[Pipeline])

    def update(
        self,
        id: str,
        *,
        conf: PipelineConfParam,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[Pipeline]]:
        """Update a Pipeline.

        Update the specified Pipeline. Provide a complete representation —
        this endpoint does not support partial updates; omitted fields are removed.

        Args:
            id: The `id` of the Pipeline to update.
            conf: Configuration for the Pipeline, including functions and settings.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the updated Pipeline.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id, "conf": conf}
        return self._patch(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[Pipeline], json=body)

    async def update_async(
        self,
        id: str,
        *,
        conf: PipelineConfParam,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[Pipeline]]:
        """Update a Pipeline (async).

        Update the specified Pipeline. Provide a complete representation —
        this endpoint does not support partial updates; omitted fields are removed.

        Args:
            id: The `id` of the Pipeline to update.
            conf: Configuration for the Pipeline, including functions and settings.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the updated Pipeline.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id, "conf": conf}
        return await self._patch_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[Pipeline], json=body)

    def delete(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[Pipeline]]:
        """Delete a Pipeline.

        Delete the specified Pipeline.

        Args:
            id: The `id` of the Pipeline to delete.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the deleted Pipeline.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._delete(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[Pipeline])

    async def delete_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[Pipeline]]:
        """Delete a Pipeline (async).

        Delete the specified Pipeline.

        Args:
            id: The `id` of the Pipeline to delete.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the deleted Pipeline.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._delete_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[Pipeline])
