"""Routes resource."""
from __future__ import annotations

from typing import Any, List

from .._response import SDKResponse

from ..models import PaginatedResponse, RouteCommentParam, RouteConfParam, RouteGroupParam, Routes
from ._base import BaseResource



class RoutesResource(BaseResource):
    """Manage data routing rules connecting sources to pipelines and destinations."""

    def _base(self, pack: str | None) -> str:
        return f"/p/{pack}/routes" if pack else "/routes"

    def list(
        self,
        *,
        pack: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[Routes]]:
        """List all Routes.

        Get a list of all Routes.

        Args:
            pack: Pack ID. If provided, scopes the operation to the specified Pack.
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing a list of Routes objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get(self._base(pack), cast_to=PaginatedResponse[Routes], params=params or None)

    async def list_async(
        self,
        *,
        pack: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[Routes]]:
        """List all Routes (async).

        Get a list of all Routes.

        Args:
            pack: Pack ID. If provided, scopes the operation to the specified Pack.
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing a list of Routes objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return await self._get_async(self._base(pack), cast_to=PaginatedResponse[Routes], params=params or None)

    def get(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[Routes]]:
        """Get a Routing table.

        Get the specified Routing table.

        Args:
            id: The `id` of the Routing table to get. The supported value is `default`.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested Routes.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Routing table not found. The specified id does not match any stored Routing table.
            ServerError (500): Unexpected server error.
        """
        return self._get(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[Routes])

    async def get_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[Routes]]:
        """Get a Routing table (async).

        Get the specified Routing table.

        Args:
            id: The `id` of the Routing table to get. The supported value is `default`.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested Routes.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Routing table not found. The specified id does not match any stored Routing table.
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[Routes])

    def update(
        self,
        id: str,
        *,
        routes: List[RouteConfParam],
        comments: List[RouteCommentParam] | None = None,
        groups: dict[str, RouteGroupParam] | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[Routes]]:
        """Update a Routing table.

        Update the specified Routing table.

        Provide a complete representation of the Routing table that you want to
        update in the request body.

        This endpoint does not support partial updates. Cribl removes any omitted
        fields when updating the Routing table.

        Confirm that the configuration in your request body is correct before
        sending the request. If the configuration is incorrect, the updated Routing
        table might not function as expected.

        Cribl also removes any omitted Routes when updating the Routing table.

        Args:
            id: The `id` of the Routing table to update. The supported value is `default`.
            routes: Array of Route configurations that define how events are processed
                and routed.
            comments: Array of user-provided comments that describe or annotate Routes.
            groups: Information about the Route Groups that the Route is associated
                with.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the updated Routes.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Routing table not found. The specified id does not match any stored Routing table.
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id, "routes": routes}
        if comments is not None:
            body["comments"] = comments
        if groups is not None:
            body["groups"] = groups
        return self._patch(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[Routes], json=body)

    async def update_async(
        self,
        id: str,
        *,
        routes: List[RouteConfParam],
        comments: List[RouteCommentParam] | None = None,
        groups: dict[str, RouteGroupParam] | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[Routes]]:
        """Update a Routing table (async).

        Update the specified Routing table.

        Provide a complete representation of the Routing table that you want to
        update in the request body.

        This endpoint does not support partial updates. Cribl removes any omitted
        fields when updating the Routing table.

        Confirm that the configuration in your request body is correct before
        sending the request. If the configuration is incorrect, the updated Routing
        table might not function as expected.

        Cribl also removes any omitted Routes when updating the Routing table.

        Args:
            id: The `id` of the Routing table to update. The supported value is `default`.
            routes: Array of Route configurations that define how events are processed
                and routed.
            comments: Array of user-provided comments that describe or annotate Routes.
            groups: Information about the Route Groups that the Route is associated
                with.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the updated Routes.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Routing table not found. The specified id does not match any stored Routing table.
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id, "routes": routes}
        if comments is not None:
            body["comments"] = comments
        if groups is not None:
            body["groups"] = groups
        return await self._patch_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[Routes], json=body)

    def append(
        self,
        id: str,
        *,
        routes: List[RouteConfParam],
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[Routes]]:
        """Add a Route to the end of the Routing table.

        Add a Route to the end of the specified Routing table.

        Args:
            id: The `id` of the Routing table to add the Route to. The supported
                value is `default`.
            routes: Route configurations to append to the Routing table.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing Routes objects.

        Raises:
            ValidationError (400): Failed validation or malformed input. The request body must be an array of Route configurations.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Routing table not found. The specified id does not match any stored Routing table.
            ServerError (500): Unexpected server error.
        """
        return self._post(f"{self._base(pack)}/{id}/append", cast_to=PaginatedResponse[Routes], json=routes)

    async def append_async(
        self,
        id: str,
        *,
        routes: List[RouteConfParam],
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[Routes]]:
        """Add a Route to the end of the Routing table (async).

        Add a Route to the end of the specified Routing table.

        Args:
            id: The `id` of the Routing table to add the Route to. The supported
                value is `default`.
            routes: Route configurations to append to the Routing table.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing Routes objects.

        Raises:
            ValidationError (400): Failed validation or malformed input. The request body must be an array of Route configurations.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Routing table not found. The specified id does not match any stored Routing table.
            ServerError (500): Unexpected server error.
        """
        return await self._post_async(f"{self._base(pack)}/{id}/append", cast_to=PaginatedResponse[Routes], json=routes)
