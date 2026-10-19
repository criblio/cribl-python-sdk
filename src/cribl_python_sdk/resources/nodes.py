"""Nodes resource."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, List

from .._response import SDKResponse
from ..models import DistributedSummary, MasterWorkerEntry, PaginatedResponse, RestartResponse
from ._base import BaseResource

if TYPE_CHECKING:
    from ..client import Cribl



class NodesSummariesResource(BaseResource):
    """Summary operations (`nodes.summaries`)."""

    def get(
        self,
        *,
        product: Literal["stream", "edge"] = "stream",
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[DistributedSummary]]:
        """Get a summary of the deployment for a Cribl product.

        Get a summary of the deployment for the specified Cribl product (Stream
        or Edge).

        The summary includes a count of Worker Groups or Edge Fleets and
        resources such as Pipelines, Routes, Sources, and Destinations. For
        Distributed deployments, the summary also includes a count and
        statistics for Worker or Edge Nodes.

        Args:
            product: Name of the Cribl product to get the summary for. Valid values: "stream", "edge". Default: "stream".
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing the requested DistributedSummary.

        Raises:
            ValidationError (400): Failed validation or malformed input if the product is not "stream" or "edge".
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized or licensed to perform this action.
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get(f"/products/{product}/summary", cast_to=PaginatedResponse[DistributedSummary], params=params or None)

    async def get_async(
        self,
        *,
        product: Literal["stream", "edge"] = "stream",
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[DistributedSummary]]:
        """Get a summary of the deployment for a Cribl product (async).

        Get a summary of the deployment for the specified Cribl product (Stream
        or Edge).

        The summary includes a count of Worker Groups or Edge Fleets and
        resources such as Pipelines, Routes, Sources, and Destinations. For
        Distributed deployments, the summary also includes a count and
        statistics for Worker or Edge Nodes.

        Args:
            product: Name of the Cribl product to get the summary for. Valid values: "stream", "edge". Default: "stream".
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing the requested DistributedSummary.

        Raises:
            ValidationError (400): Failed validation or malformed input if the product is not "stream" or "edge".
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized or licensed to perform this action.
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return await self._get_async(f"/products/{product}/summary", cast_to=PaginatedResponse[DistributedSummary], params=params or None)


class NodesResource(BaseResource):
    """Manage Worker, Edge, and Outpost Nodes."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.summaries = NodesSummariesResource(client)

    def list(
        self,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        filterExp: str | None = None,
        sortExp: str | None = None,
        filter: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> SDKResponse[PaginatedResponse[MasterWorkerEntry]]:
        """Get detailed metadata for Worker, Edge, or Outpost Nodes.

        Get detailed metadata for Worker, Edge, or Outpost Nodes for the
        specified Cribl product.

        Args:
            product: Name of the Cribl product to get Worker, Edge, or Outpost Nodes for. Valid values: "stream", "edge", "outpost". Default: "stream".
            filterExp: Filter expression to evaluate against Nodes for inclusion
                in the response (for example, `status=='healthy'`).
            sortExp: Sorting expression to evaluate against Nodes to specify the
                sort order for the response.
            filter: JSON-stringified filter object to evaluate against Nodes for
                inclusion in the response (for example,
                `{"field":"status","op":"eq","value":"healthy"}`).
            sort: JSON-stringified sorting object to evaluate against Nodes to
                specify the sort order for the response.
            limit: Maximum number of Nodes to return in the response for this
                request. Use with `offset` to paginate the response into
                manageable batches.
            offset: Starting point from which to retrieve results for this
                request. Use with `limit` to paginate the response into
                manageable batches.

        Returns:
            (200) PaginatedResponse containing a list of MasterWorkerEntry objects.

        Raises:
            ValidationError (400): Failed validation or malformed input if the product is not "stream", "edge", or "outpost".
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized or licensed to perform this action.
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if filterExp is not None:
            params["filterExp"] = filterExp
        if sortExp is not None:
            params["sortExp"] = sortExp
        if filter is not None:
            params["filter"] = filter
        if sort is not None:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._get(f"/products/{product}/workers", cast_to=PaginatedResponse[MasterWorkerEntry], params=params or None)

    async def list_async(
        self,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        filterExp: str | None = None,
        sortExp: str | None = None,
        filter: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> SDKResponse[PaginatedResponse[MasterWorkerEntry]]:
        """Get detailed metadata for Worker, Edge, or Outpost Nodes (async).

        Get detailed metadata for Worker, Edge, or Outpost Nodes for the
        specified Cribl product.

        Args:
            product: Name of the Cribl product to get Worker, Edge, or Outpost Nodes for. Valid values: "stream", "edge", "outpost". Default: "stream".
            filterExp: Filter expression to evaluate against Nodes for inclusion
                in the response (for example, `status=='healthy'`).
            sortExp: Sorting expression to evaluate against Nodes to specify the
                sort order for the response.
            filter: JSON-stringified filter object to evaluate against Nodes for
                inclusion in the response (for example,
                `{"field":"status","op":"eq","value":"healthy"}`).
            sort: JSON-stringified sorting object to evaluate against Nodes to
                specify the sort order for the response.
            limit: Maximum number of Nodes to return in the response for this
                request. Use with `offset` to paginate the response into
                manageable batches.
            offset: Starting point from which to retrieve results for this
                request. Use with `limit` to paginate the response into
                manageable batches.

        Returns:
            (200) PaginatedResponse containing a list of MasterWorkerEntry objects.

        Raises:
            ValidationError (400): Failed validation or malformed input if the product is not "stream", "edge", or "outpost".
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized or licensed to perform this action.
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if filterExp is not None:
            params["filterExp"] = filterExp
        if sortExp is not None:
            params["sortExp"] = sortExp
        if filter is not None:
            params["filter"] = filter
        if sort is not None:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return await self._get_async(f"/products/{product}/workers", cast_to=PaginatedResponse[MasterWorkerEntry], params=params or None)

    def get(self, id: str, *, product: Literal["stream", "edge", "outpost"] = "stream") -> SDKResponse[PaginatedResponse[MasterWorkerEntry]]:
        """Get detailed metadata for a Worker, Edge, or Outpost Node.

        Get detailed metadata for the specified Worker, Edge, or Outpost Node
        for the specified Cribl product.

        Args:
            id: The `id` of the Node to get the metadata for.
            product: Name of the Cribl product that contains the Node. Valid values: "stream", "edge", "outpost". Default: "stream".

        Returns:
            (200) PaginatedResponse containing the requested MasterWorkerEntry.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized or licensed to perform this action.
            ServerError (500): Unexpected server error.
        """
        return self._get(f"/products/{product}/workers/{id}", cast_to=PaginatedResponse[MasterWorkerEntry])

    async def get_async(self, id: str, *, product: Literal["stream", "edge", "outpost"] = "stream") -> SDKResponse[PaginatedResponse[MasterWorkerEntry]]:
        """Get detailed metadata for a Worker, Edge, or Outpost Node (async).

        Get detailed metadata for the specified Worker, Edge, or Outpost Node
        for the specified Cribl product.

        Args:
            id: The `id` of the Node to get the metadata for.
            product: Name of the Cribl product that contains the Node. Valid values: "stream", "edge", "outpost". Default: "stream".

        Returns:
            (200) PaginatedResponse containing the requested MasterWorkerEntry.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized or licensed to perform this action.
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"/products/{product}/workers/{id}", cast_to=PaginatedResponse[MasterWorkerEntry])

    def restart(self, *, product: Literal["stream", "edge", "outpost"] = "stream", guids: List[str]) -> SDKResponse[PaginatedResponse[RestartResponse]]:
        """Restart Worker, Edge, or Outpost Nodes.

        Restart all Worker, Edge, or Outpost Nodes for the specified Cribl
        product.

        Args:
            product: Name of the Cribl product whose Worker, Edge, or Outpost Nodes you want to restart. Valid values: "stream", "edge", "outpost". Default: "stream".
            guids: GUIDs of the Worker or Edge Nodes to restart.

        Returns:
            (200) PaginatedResponse containing RestartResponse objects with id, status, and optional message.

        Raises:
            ValidationError (400): Failed validation or malformed input if the product is not "stream", "edge", or "outpost".
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized or licensed to perform this action.
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"guids": guids}
        return self._patch(f"/products/{product}/workers/restart", cast_to=PaginatedResponse[RestartResponse], json=body)

    async def restart_async(self, *, product: Literal["stream", "edge", "outpost"] = "stream", guids: List[str]) -> SDKResponse[PaginatedResponse[RestartResponse]]:
        """Restart Worker, Edge, or Outpost Nodes (async).

        Restart all Worker, Edge, or Outpost Nodes for the specified Cribl
        product.

        Args:
            product: Name of the Cribl product whose Worker, Edge, or Outpost Nodes you want to restart. Valid values: "stream", "edge", "outpost". Default: "stream".
            guids: GUIDs of the Worker or Edge Nodes to restart.

        Returns:
            (200) PaginatedResponse containing RestartResponse objects with id, status, and optional message.

        Raises:
            ValidationError (400): Failed validation or malformed input if the product is not "stream", "edge", or "outpost".
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized or licensed to perform this action.
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"guids": guids}
        return await self._patch_async(f"/products/{product}/workers/restart", cast_to=PaginatedResponse[RestartResponse], json=body)

    def count(self, *, product: Literal["stream", "edge", "outpost"] = "stream", filterExp: str | None = None) -> SDKResponse[PaginatedResponse[int]]:
        """Get a count of Worker, Edge, or Outpost Nodes.

        Get a count of all Worker, Edge, or Outpost Nodes for the specified
        Cribl product.

        Args:
            product: Name of the Cribl product to get the count of Worker, Edge, or Outpost Nodes for. Valid values: "stream", "edge", "outpost". Default: "stream".
            filterExp: Filter expression to evaluate against Nodes for inclusion
                in the response (for example, `status=='healthy'`).

        Returns:
            (200) PaginatedResponse containing the requested int.

        Raises:
            ValidationError (400): Failed validation or malformed input if the product is not "stream", "edge", or "outpost".
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized or licensed to perform this action.
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if filterExp is not None:
            params["filterExp"] = filterExp
        return self._get(f"/products/{product}/summary/workers", cast_to=PaginatedResponse[int], params=params or None)

    async def count_async(self, *, product: Literal["stream", "edge", "outpost"] = "stream", filterExp: str | None = None) -> SDKResponse[PaginatedResponse[int]]:
        """Get a count of Worker, Edge, or Outpost Nodes (async).

        Get a count of all Worker, Edge, or Outpost Nodes for the specified
        Cribl product.

        Args:
            product: Name of the Cribl product to get the count of Worker, Edge, or Outpost Nodes for. Valid values: "stream", "edge", "outpost". Default: "stream".
            filterExp: Filter expression to evaluate against Nodes for inclusion
                in the response (for example, `status=='healthy'`).

        Returns:
            (200) PaginatedResponse containing the requested int.

        Raises:
            ValidationError (400): Failed validation or malformed input if the product is not "stream", "edge", or "outpost".
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            AuthorizationError (403): Not authorized or licensed to perform this action.
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if filterExp is not None:
            params["filterExp"] = filterExp
        return await self._get_async(f"/products/{product}/summary/workers", cast_to=PaginatedResponse[int], params=params or None)
