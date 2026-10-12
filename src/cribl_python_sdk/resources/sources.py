"""Sources resource."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .._response import SDKResponse
from ..models import HecTokenMetadataParam, Input, InputStatus, JobInfo, PaginatedResponse, SourceResponse
from ._base import BaseResource

if TYPE_CHECKING:
    from ..client import Cribl


def _src_base(pack: str | None) -> str:
    return f"/p/{pack}/system/inputs" if pack else "/system/inputs"


def _src_status_base(pack: str | None) -> str:
    return f"/p/{pack}/system/status/inputs" if pack else "/system/status/inputs"


class SourcesPqResource(BaseResource):
    """Persistent queue operations for Sources (`sources.pq`)."""

    def get(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[JobInfo]]:
        """Get information about the latest job to clear the persistent queue for a Source.

        Get information about the latest job to clear the persistent queue (PQ) for
        the specified Source.

        Args:
            id: The `id` of the Source to get PQ job information for.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested JobInfo.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(f"{_src_base(pack)}/{id}/pq", cast_to=PaginatedResponse[JobInfo])

    async def get_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[JobInfo]]:
        """Get information about the latest job to clear the persistent queue for a Source (async).

        Get information about the latest job to clear the persistent queue (PQ) for
        the specified Source.

        Args:
            id: The `id` of the Source to get PQ job information for.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested JobInfo.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"{_src_base(pack)}/{id}/pq", cast_to=PaginatedResponse[JobInfo])

    def clear(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[str]]:
        """Clear the persistent queue for a Source.

        Clear the persistent queue (PQ) for the specified Source.

        Args:
            id: The `id` of the Source to clear the PQ for.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing str objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._delete(f"{_src_base(pack)}/{id}/pq", cast_to=PaginatedResponse[str])

    async def clear_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[str]]:
        """Clear the persistent queue for a Source (async).

        Clear the persistent queue (PQ) for the specified Source.

        Args:
            id: The `id` of the Source to clear the PQ for.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing str objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._delete_async(f"{_src_base(pack)}/{id}/pq", cast_to=PaginatedResponse[str])


class SourcesStatusesResource(BaseResource):
    """Status operations for Sources (`sources.statuses`)."""

    def list(
        self,
        *,
        metrics: bool | None = None,
        type: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[InputStatus]]:
        """List the status of all Sources.

        List status information and optional metrics for all configured Sources in
        the Worker Group or Edge Fleet.

        Args:
            metrics: Set to `true` to include metrics for each Source. Otherwise,
                `false` (default).
            type: Set to `true` to prefix the Source `id` with the Source type.
                Otherwise, `false` (default).
            offset: Starting point from which to retrieve results for this request.
                Use with `limit` to paginate the response into manageable batches.
            limit: Maximum number of items to return in the response for this request.
                Use with `offset` to paginate the response into manageable batches.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing a list of InputStatus objects.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if metrics is not None:
            params["metrics"] = metrics
        if type is not None:
            params["type"] = type
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get(_src_status_base(pack), cast_to=PaginatedResponse[InputStatus], params=params or None)

    async def list_async(
        self,
        *,
        metrics: bool | None = None,
        type: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[InputStatus]]:
        """List the status of all Sources (async).

        List status information and optional metrics for all configured Sources in
        the Worker Group or Edge Fleet.

        Args:
            metrics: Set to `true` to include metrics for each Source. Otherwise,
                `false` (default).
            type: Set to `true` to prefix the Source `id` with the Source type.
                Otherwise, `false` (default).
            offset: Starting point from which to retrieve results for this request.
                Use with `limit` to paginate the response into manageable batches.
            limit: Maximum number of items to return in the response for this request.
                Use with `offset` to paginate the response into manageable batches.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing a list of InputStatus objects.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if metrics is not None:
            params["metrics"] = metrics
        if type is not None:
            params["type"] = type
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return await self._get_async(_src_status_base(pack), cast_to=PaginatedResponse[InputStatus], params=params or None)

    def get(
        self,
        id: str,
        *,
        metrics: bool | None = None,
        type: str | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[InputStatus]]:
        """Get the status of a Source.

        Get the status and optional metrics for the specified Source.

        Args:
            id: The `id` of the Source to get the status for.
            metrics: Set to `true` to include metrics for each Source. Otherwise,
                `false` (default).
            type: Set to `true` to prefix the Source `id` with the Source type.
                Otherwise, `false` (default).
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested InputStatus.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if metrics is not None:
            params["metrics"] = metrics
        if type is not None:
            params["type"] = type
        return self._get(f"{_src_status_base(pack)}/{id}", cast_to=PaginatedResponse[InputStatus], params=params or None)

    async def get_async(
        self,
        id: str,
        *,
        metrics: bool | None = None,
        type: str | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[InputStatus]]:
        """Get the status of a Source (async).

        Get the status and optional metrics for the specified Source.

        Args:
            id: The `id` of the Source to get the status for.
            metrics: Set to `true` to include metrics for each Source. Otherwise,
                `false` (default).
            type: Set to `true` to prefix the Source `id` with the Source type.
                Otherwise, `false` (default).
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested InputStatus.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if metrics is not None:
            params["metrics"] = metrics
        if type is not None:
            params["type"] = type
        return await self._get_async(f"{_src_status_base(pack)}/{id}", cast_to=PaginatedResponse[InputStatus], params=params or None)


class SourcesHecTokensResource(BaseResource):
    """HEC token operations for Sources (`sources.hecTokens`)."""

    def create(
        self,
        id: str,
        *,
        token: str,
        description: str | None = None,
        enabled: bool | None = None,
        allowedIndexesAtToken: list[str] | None = None,
        metadata: list[HecTokenMetadataParam] | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Add an HEC token and optional metadata to a Splunk HEC Source.

        Add an HEC token and optional metadata to the specified Splunk HEC Source.

        Args:
            id: The `id` of the Splunk HEC Source.
            token: The HEC token value to add to the Splunk HEC Source.
            description: Brief description for the HEC token.
            enabled: If `true`, the HEC token is enabled. Otherwise, `false`.
            allowedIndexesAtToken: List of index names that the HEC token is allowed
                to write to.
            metadata: Array of key-value pairs to associate with the HEC token for
                tagging, categorization, or providing additional context. Each item in
                the array is an object with a `name` and a `value`.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing Source objects.

        Raises:
            ValidationError (400): Failed validation or malformed input — Source not found, source type is not splunk_hec, or request payload is invalid.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"token": token}
        if description is not None:
            body["description"] = description
        if enabled is not None:
            body["enabled"] = enabled
        if allowedIndexesAtToken is not None:
            body["allowedIndexesAtToken"] = allowedIndexesAtToken
        if metadata is not None:
            body["metadata"] = metadata
        return self._post(f"{_src_base(pack)}/{id}/hectoken", cast_to=PaginatedResponse[SourceResponse], json=body)

    async def create_async(
        self,
        id: str,
        *,
        token: str,
        description: str | None = None,
        enabled: bool | None = None,
        allowedIndexesAtToken: list[str] | None = None,
        metadata: list[HecTokenMetadataParam] | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Add an HEC token and optional metadata to a Splunk HEC Source (async).

        Add an HEC token and optional metadata to the specified Splunk HEC Source.

        Args:
            id: The `id` of the Splunk HEC Source.
            token: The HEC token value to add to the Splunk HEC Source.
            description: Brief description for the HEC token.
            enabled: If `true`, the HEC token is enabled. Otherwise, `false`.
            allowedIndexesAtToken: List of index names that the HEC token is allowed
                to write to.
            metadata: Array of key-value pairs to associate with the HEC token for
                tagging, categorization, or providing additional context. Each item in
                the array is an object with a `name` and a `value`.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing Source objects.

        Raises:
            ValidationError (400): Failed validation or malformed input — Source not found, source type is not splunk_hec, or request payload is invalid.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"token": token}
        if description is not None:
            body["description"] = description
        if enabled is not None:
            body["enabled"] = enabled
        if allowedIndexesAtToken is not None:
            body["allowedIndexesAtToken"] = allowedIndexesAtToken
        if metadata is not None:
            body["metadata"] = metadata
        return await self._post_async(f"{_src_base(pack)}/{id}/hectoken", cast_to=PaginatedResponse[SourceResponse], json=body)

    def update(
        self,
        id: str,
        token: str,
        *,
        description: str | None = None,
        enabled: bool | None = None,
        allowedIndexesAtToken: list[str] | None = None,
        metadata: list[HecTokenMetadataParam] | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Update metadata for an HEC token for a Splunk HEC Source.

        Update the metadata for the specified HEC token for the specified Splunk HEC
        Source.

        Args:
            id: The `id` of the Splunk HEC Source.
            token: The HEC token value whose metadata you want to update. Must match
                an existing token on the Source.
            description: Brief description for the HEC token.
            enabled: If `true`, the HEC token is enabled. Otherwise, `false`.
            allowedIndexesAtToken: List of index names that the HEC token is allowed
                to write to.
            metadata: Array of key-value pairs to associate with the HEC token for
                tagging, categorization, or providing additional context. Each item in
                the array is an object with a `name` and a `value`.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the updated Source.

        Raises:
            ValidationError (400): Failed validation or malformed input — Source not found, source type is not splunk_hec, or request payload is invalid.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {}
        if description is not None:
            body["description"] = description
        if enabled is not None:
            body["enabled"] = enabled
        if allowedIndexesAtToken is not None:
            body["allowedIndexesAtToken"] = allowedIndexesAtToken
        if metadata is not None:
            body["metadata"] = metadata
        return self._patch(f"{_src_base(pack)}/{id}/hectoken/{token}", cast_to=PaginatedResponse[SourceResponse], json=body)

    async def update_async(
        self,
        id: str,
        token: str,
        *,
        description: str | None = None,
        enabled: bool | None = None,
        allowedIndexesAtToken: list[str] | None = None,
        metadata: list[HecTokenMetadataParam] | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Update metadata for an HEC token for a Splunk HEC Source (async).

        Update the metadata for the specified HEC token for the specified Splunk HEC
        Source.

        Args:
            id: The `id` of the Splunk HEC Source.
            token: The HEC token value whose metadata you want to update. Must match
                an existing token on the Source.
            description: Brief description for the HEC token.
            enabled: If `true`, the HEC token is enabled. Otherwise, `false`.
            allowedIndexesAtToken: List of index names that the HEC token is allowed
                to write to.
            metadata: Array of key-value pairs to associate with the HEC token for
                tagging, categorization, or providing additional context. Each item in
                the array is an object with a `name` and a `value`.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the updated Source.

        Raises:
            ValidationError (400): Failed validation or malformed input — Source not found, source type is not splunk_hec, or request payload is invalid.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {}
        if description is not None:
            body["description"] = description
        if enabled is not None:
            body["enabled"] = enabled
        if allowedIndexesAtToken is not None:
            body["allowedIndexesAtToken"] = allowedIndexesAtToken
        if metadata is not None:
            body["metadata"] = metadata
        return await self._patch_async(f"{_src_base(pack)}/{id}/hectoken/{token}", cast_to=PaginatedResponse[SourceResponse], json=body)


class SourcesResource(BaseResource):
    """Manage data sources (inputs)."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.pq = SourcesPqResource(client)
        self.statuses = SourcesStatusesResource(client)
        self.hec_tokens = SourcesHecTokensResource(client)

    def _base(self, pack: str | None) -> str:
        return _src_base(pack)

    def _status_base(self, pack: str | None) -> str:
        return _src_status_base(pack)

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def list(
        self,
        *,
        type: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """List all Sources.

        Get a list of all Sources.

        Args:
            type: Type of Source to include in the results. Each request can include
                only one `type` parameter; multiple parameters per request are not
                supported.
            offset: Pagination offset
            limit: Maximum number of items to return
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing a list of Source objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if type is not None:
            params["type"] = type
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get(self._base(pack), cast_to=PaginatedResponse[SourceResponse], params=params or None)

    async def list_async(
        self,
        *,
        type: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """List all Sources (async).

        Get a list of all Sources.

        Args:
            type: Type of Source to include in the results. Each request can include
                only one `type` parameter; multiple parameters per request are not
                supported.
            offset: Pagination offset
            limit: Maximum number of items to return
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing a list of Source objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if type is not None:
            params["type"] = type
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return await self._get_async(self._base(pack), cast_to=PaginatedResponse[SourceResponse], params=params or None)

    def create(
        self,
        source: Input | dict[str, object],
        *,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Create a Source.

        Create a new Source. The system-managed provenance field (JSON
        `criblSourceProvenance`) must be omitted from the request body.

        Args:
            source: Source configuration as a typed Input model (e.g.
                InputSyslog, InputKafka) or a plain dict.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the created Source.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = source.model_dump(exclude_none=True) if hasattr(source, "model_dump") else source # pyright: ignore[reportAttributeAccessIssue]
        return self._post(self._base(pack), cast_to=PaginatedResponse[SourceResponse], json=body)

    async def create_async(
        self,
        source: Input | dict[str, object],
        *,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Create a Source (async).

        Create a new Source. The system-managed provenance field (JSON
        `criblSourceProvenance`) must be omitted from the request body.

        Args:
            source: Source configuration as a typed Input model (e.g.
                InputSyslog, InputKafka) or a plain dict.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the created Source.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = source.model_dump(exclude_none=True) if hasattr(source, "model_dump") else source # pyright: ignore[reportAttributeAccessIssue]
        return await self._post_async(self._base(pack), cast_to=PaginatedResponse[SourceResponse], json=body)

    def get(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Get a Source.

        Get the specified Source.

        Args:
            id: The `id` of the Source to get.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested Source.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): The requested resource does not exist — Source not found.
            ServerError (500): Unexpected server error.
        """
        return self._get(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[SourceResponse])

    async def get_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Get a Source (async).

        Get the specified Source.

        Args:
            id: The `id` of the Source to get.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested Source.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): The requested resource does not exist — Source not found.
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[SourceResponse])

    def update(
        self,
        id: str,
        source: Input | dict[str, object],
        *,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Update a Source.

        Update the specified Source. Provide a complete representation of the
        Source in the request body — this endpoint does not support partial
        updates; omitted fields are removed.

        Args:
            id: The `id` of the Source to update.
            source: Complete Source configuration as a typed Input model or dict.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the updated Source.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = source.model_dump(exclude_none=True) if hasattr(source, "model_dump") else dict(source) # pyright: ignore[reportAttributeAccessIssue]
        body["id"] = id
        return self._patch(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[SourceResponse], json=body)

    async def update_async(
        self,
        id: str,
        source: Input | dict[str, object],
        *,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Update a Source (async).

        Update the specified Source. Provide a complete representation of the
        Source in the request body — this endpoint does not support partial
        updates; omitted fields are removed.

        Args:
            id: The `id` of the Source to update.
            source: Complete Source configuration as a typed Input model or dict.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the updated Source.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = source.model_dump(exclude_none=True) if hasattr(source, "model_dump") else dict(source) # pyright: ignore[reportAttributeAccessIssue]
        body["id"] = id
        return await self._patch_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[SourceResponse], json=body)

    def delete(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Delete a Source.

        Delete the specified Source.

        Args:
            id: The `id` of the Source to delete.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the deleted Source.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._delete(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[SourceResponse])

    async def delete_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[SourceResponse]]:
        """Delete a Source (async).

        Delete the specified Source.

        Args:
            id: The `id` of the Source to delete.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the deleted Source.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._delete_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[SourceResponse])
