"""Functions resource."""
from __future__ import annotations

from typing import Any

from .._response import SDKResponse

from ..models import FunctionDef, PaginatedResponse
from ._base import BaseResource


class FunctionsResource(BaseResource):
    """List available Cribl processing functions."""

    def list(
        self,
        *,
        showHidden: bool | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[FunctionDef]]:
        """List all Functions.

        Get a list of all Functions.

        Args:
            showHidden: If `true`, include hidden Functions in the response.
                Otherwise, hidden Functions are excluded.
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing a list of FunctionDef objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if showHidden is not None:
            params["showHidden"] = showHidden
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get("/functions", cast_to=PaginatedResponse[FunctionDef], params=params or None)

    async def list_async(
        self,
        *,
        showHidden: bool | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[FunctionDef]]:
        """List all Functions (async).

        Get a list of all Functions.

        Args:
            showHidden: If `true`, include hidden Functions in the response.
                Otherwise, hidden Functions are excluded.
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing a list of FunctionDef objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if showHidden is not None:
            params["showHidden"] = showHidden
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return await self._get_async("/functions", cast_to=PaginatedResponse[FunctionDef], params=params or None)

    def get(self, id: str) -> SDKResponse[PaginatedResponse[FunctionDef]]:
        """Get a Function.

        Get the specified Function.

        Args:
            id: The `id` of the Function to get.

        Returns:
            (200) PaginatedResponse containing the requested FunctionDef.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(f"/functions/{id}", cast_to=PaginatedResponse[FunctionDef])

    async def get_async(self, id: str) -> SDKResponse[PaginatedResponse[FunctionDef]]:
        """Get a Function (async).

        Get the specified Function.

        Args:
            id: The `id` of the Function to get.

        Returns:
            (200) PaginatedResponse containing the requested FunctionDef.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"/functions/{id}", cast_to=PaginatedResponse[FunctionDef])
