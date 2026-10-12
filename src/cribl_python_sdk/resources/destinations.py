"""Destinations resource."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from .._response import SDKResponse
from ..models import DestinationResponse, JobInfo, Output, OutputSamplesResponse, OutputStatus, OutputTestResponse, PaginatedResponse
from ._base import BaseResource

if TYPE_CHECKING:
    from ..client import Cribl

DestinationType = Literal[
    "default", "router", "tcpjson", "splunk", "splunk_lb", "splunk_hec", "syslog",
    "filesystem", "s3", "azure_blob", "azure_data_explorer", "sentinel", "azure_logs",
    "kafka", "confluent_cloud", "msk", "kinesis", "elastic", "elastic_cloud",
    "microsoft_fabric", "cloudflare_r2", "honeycomb", "newrelic", "newrelic_events",
    "snmp", "influxdb", "minio", "devnull", "cloudwatch", "azure_eventhub", "statsd",
    "statsd_ext", "graphite", "wavefront", "signalfx", "sqs", "google_cloud_storage",
    "sumo_logic", "datadog", "webhook", "prometheus", "amazon_managed_prometheus",
    "google_pubsub", "google_chronicle", "chronicle", "google_cloud_observability",
    "google_bigquery", "grafana_cloud", "loki", "open_telemetry", "service_now",
    "dynatrace_otlp", "sentinel_one_ai_siem", "dataset", "ring", "humio_hec",
    "crowdstrike_next_gen_siem", "cribl_http", "cribl_tcp", "cribl_search_engine",
    "google_cloud_logging", "sns", "dl_s3", "security_lake", "cribl_lake", "exabeam",
    "disk_spool", "click_house", "customer_metrics_storage", "local_search_storage",
    "xsiam", "netflow", "dynatrace_http", "databricks", "wiz_hec", "nutanix_objects",
    "storj_s3", "alphasoc_s3", "dell_s3", "cloudian_s3", "scality_s3",
    "alibaba_cloud_s3", "snowflake_streaming", "ibm_cloud_s3",
    "databricks_zerobus", "traversal_otlp", "securonix",
]



def _dest_base(pack: str | None) -> str:
    return f"/p/{pack}/system/outputs" if pack else "/system/outputs"


def _dest_status_base(pack: str | None) -> str:
    return f"/p/{pack}/system/status/outputs" if pack else "/system/status/outputs"


class DestinationsPqResource(BaseResource):
    """Persistent queue operations for Destinations (`destinations.pq`)."""

    def get(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[JobInfo]]:
        """Get information about the latest job to clear the persistent queue for a Destination.

        Get information about the latest job to clear the persistent queue (PQ) for
        the specified Destination.

        Args:
            id: The `id` of the Destination to get PQ job information for.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested JobInfo.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(f"{_dest_base(pack)}/{id}/pq", cast_to=PaginatedResponse[JobInfo])

    async def get_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[JobInfo]]:
        """Get information about the latest job to clear the persistent queue for a Destination (async).

        Get information about the latest job to clear the persistent queue (PQ) for
        the specified Destination.

        Args:
            id: The `id` of the Destination to get PQ job information for.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested JobInfo.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"{_dest_base(pack)}/{id}/pq", cast_to=PaginatedResponse[JobInfo])

    def clear(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[str]]:
        """Clear the persistent queue for a Destination.

        Clear the persistent queue (PQ) for the specified Destination.

        Args:
            id: The `id` of the Destination to clear the PQ for.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing str objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._delete(f"{_dest_base(pack)}/{id}/pq", cast_to=PaginatedResponse[str])

    async def clear_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[str]]:
        """Clear the persistent queue for a Destination (async).

        Clear the persistent queue (PQ) for the specified Destination.

        Args:
            id: The `id` of the Destination to clear the PQ for.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing str objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._delete_async(f"{_dest_base(pack)}/{id}/pq", cast_to=PaginatedResponse[str])


class DestinationsSamplesResource(BaseResource):
    """Sample/test operations for Destinations (`destinations.samples`)."""

    def get(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[OutputSamplesResponse]]:
        """Get sample event data for a Destination.

        Get sample event data for the specified Destination to validate the
        configuration or test connectivity.

        Args:
            id: The `id` of the Destination to get sample event data for.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested OutputSamplesResponse.

        Raises:
            ValidationError (400): Failed validation or malformed input — invalid request or Destination error.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(f"{_dest_base(pack)}/{id}/samples", cast_to=PaginatedResponse[OutputSamplesResponse])

    async def get_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[OutputSamplesResponse]]:
        """Get sample event data for a Destination (async).

        Get sample event data for the specified Destination to validate the
        configuration or test connectivity.

        Args:
            id: The `id` of the Destination to get sample event data for.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested OutputSamplesResponse.

        Raises:
            ValidationError (400): Failed validation or malformed input — invalid request or Destination error.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"{_dest_base(pack)}/{id}/samples", cast_to=PaginatedResponse[OutputSamplesResponse])

    def create(
        self,
        id: str,
        *,
        events: list[dict[str, Any]],
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[OutputTestResponse]]:
        """Send sample event data to a Destination.

        Send sample event data to the specified Destination to validate the
        configuration or test connectivity.

        Args:
            id: The `id` of the Destination to send sample event data to.
            events: Array of event objects to send to the Destination for testing.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing OutputTestResponse objects.

        Raises:
            ValidationError (400): Failed validation or malformed input — missing or invalid events.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"events": events}
        return self._post(f"{_dest_base(pack)}/{id}/test", cast_to=PaginatedResponse[OutputTestResponse], json=body)

    async def create_async(
        self,
        id: str,
        *,
        events: list[dict[str, Any]],
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[OutputTestResponse]]:
        """Send sample event data to a Destination (async).

        Send sample event data to the specified Destination to validate the
        configuration or test connectivity.

        Args:
            id: The `id` of the Destination to send sample event data to.
            events: Array of event objects to send to the Destination for testing.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing OutputTestResponse objects.

        Raises:
            ValidationError (400): Failed validation or malformed input — missing or invalid events.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"events": events}
        return await self._post_async(f"{_dest_base(pack)}/{id}/test", cast_to=PaginatedResponse[OutputTestResponse], json=body)


class DestinationsStatusesResource(BaseResource):
    """Status operations for Destinations (`destinations.statuses`)."""

    def list(
        self,
        *,
        metrics: bool | None = None,
        type: bool | None = None,
        offset: int | None = None,
        limit: int | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[OutputStatus]]:
        """List the status of all Destinations.

        List status information and optional metrics for all configured Destinations
        in the Worker Group or Edge Fleet.

        Args:
            metrics: Set to `true` to include metrics for each Destination. Otherwise,
                `false` (default).
            type: Set to `true` to prefix the Destination `id` with the Destination
                type. Otherwise, `false` (default).
            offset: Starting point from which to retrieve results for this request.
                Use with `limit` to paginate the response into manageable batches.
            limit: Maximum number of items to return in the response for this request.
                Use with `offset` to paginate the response into manageable batches.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing a list of OutputStatus objects.

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
        return self._get(_dest_status_base(pack), cast_to=PaginatedResponse[OutputStatus], params=params or None)

    async def list_async(
        self,
        *,
        metrics: bool | None = None,
        type: bool | None = None,
        offset: int | None = None,
        limit: int | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[OutputStatus]]:
        """List the status of all Destinations (async).

        List status information and optional metrics for all configured Destinations
        in the Worker Group or Edge Fleet.

        Args:
            metrics: Set to `true` to include metrics for each Destination. Otherwise,
                `false` (default).
            type: Set to `true` to prefix the Destination `id` with the Destination
                type. Otherwise, `false` (default).
            offset: Starting point from which to retrieve results for this request.
                Use with `limit` to paginate the response into manageable batches.
            limit: Maximum number of items to return in the response for this request.
                Use with `offset` to paginate the response into manageable batches.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing a list of OutputStatus objects.

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
        return await self._get_async(_dest_status_base(pack), cast_to=PaginatedResponse[OutputStatus], params=params or None)

    def get(
        self,
        id: str,
        *,
        metrics: bool | None = None,
        type: bool | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[OutputStatus]]:
        """Get the status of a Destination.

        Get the status and optional metrics for the specified Destination.

        Args:
            id: The `id` of the Destination to get the status for.
            metrics: Set to `true` to include metrics for each Destination. Otherwise,
                `false` (default).
            type: Set to `true` to prefix the Destination `id` with the Destination
                type. Otherwise, `false` (default).
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested OutputStatus.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if metrics is not None:
            params["metrics"] = metrics
        if type is not None:
            params["type"] = type
        return self._get(f"{_dest_status_base(pack)}/{id}", cast_to=PaginatedResponse[OutputStatus], params=params or None)

    async def get_async(
        self,
        id: str,
        *,
        metrics: bool | None = None,
        type: bool | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[OutputStatus]]:
        """Get the status of a Destination (async).

        Get the status and optional metrics for the specified Destination.

        Args:
            id: The `id` of the Destination to get the status for.
            metrics: Set to `true` to include metrics for each Destination. Otherwise,
                `false` (default).
            type: Set to `true` to prefix the Destination `id` with the Destination
                type. Otherwise, `false` (default).
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested OutputStatus.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if metrics is not None:
            params["metrics"] = metrics
        if type is not None:
            params["type"] = type
        return await self._get_async(f"{_dest_status_base(pack)}/{id}", cast_to=PaginatedResponse[OutputStatus], params=params or None)


class DestinationsResource(BaseResource):
    """Manage data destinations (outputs)."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.pq = DestinationsPqResource(client)
        self.samples = DestinationsSamplesResource(client)
        self.statuses = DestinationsStatusesResource(client)

    def _base(self, pack: str | None) -> str:
        return _dest_base(pack)

    def _status_base(self, pack: str | None) -> str:
        return _dest_status_base(pack)

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def list(
        self,
        *,
        type: DestinationType | None = None,
        offset: int | None = None,
        limit: int | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[DestinationResponse]]:
        """List all Destinations.

        Get a list of all Destinations.

        Args:
            type: Type of Destination to include in the results. Each request can
                include only one `type` parameter; multiple parameters per request are
                not supported.
            offset: Pagination offset
            limit: Maximum number of items to return
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing a list of Destination objects.

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
        return self._get(self._base(pack), cast_to=PaginatedResponse[DestinationResponse], params=params or None)

    async def list_async(
        self,
        *,
        type: DestinationType | None = None,
        offset: int | None = None,
        limit: int | None = None,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[DestinationResponse]]:
        """List all Destinations (async).

        Get a list of all Destinations.

        Args:
            type: Type of Destination to include in the results. Each request can
                include only one `type` parameter; multiple parameters per request are
                not supported.
            offset: Pagination offset
            limit: Maximum number of items to return
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing a list of Destination objects.

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
        return await self._get_async(self._base(pack), cast_to=PaginatedResponse[DestinationResponse], params=params or None)

    def create(
        self,
        destination: Output | dict[str, object],
        *,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[DestinationResponse]]:
        """Create a Destination.

        Create a new Destination.

        Args:
            destination: Destination configuration as a typed Output model
                (e.g. OutputS3, OutputSplunk) or a plain dict.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the created Destination.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = destination.model_dump(exclude_none=True) if hasattr(destination, "model_dump") else destination # pyright: ignore[reportAttributeAccessIssue]
        return self._post(self._base(pack), cast_to=PaginatedResponse[DestinationResponse], json=body)

    async def create_async(
        self,
        destination: Output | dict[str, object],
        *,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[DestinationResponse]]:
        """Create a Destination (async).

        Create a new Destination.

        Args:
            destination: Destination configuration as a typed Output model
                (e.g. OutputS3, OutputSplunk) or a plain dict.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the created Destination.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = destination.model_dump(exclude_none=True) if hasattr(destination, "model_dump") else destination # pyright: ignore[reportAttributeAccessIssue]
        return await self._post_async(self._base(pack), cast_to=PaginatedResponse[DestinationResponse], json=body)

    def get(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[DestinationResponse]]:
        """Get a Destination.

        Get the specified Destination.

        Args:
            id: The `id` of the Destination to get.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested Destination.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): The requested resource does not exist.
            ServerError (500): Unexpected server error.
        """
        return self._get(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[DestinationResponse])

    async def get_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[DestinationResponse]]:
        """Get a Destination (async).

        Get the specified Destination.

        Args:
            id: The `id` of the Destination to get.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the requested Destination.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): The requested resource does not exist.
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[DestinationResponse])

    def update(
        self,
        id: str,
        destination: Output | dict[str, object],
        *,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[DestinationResponse]]:
        """Update a Destination.

        Update the specified Destination. Provide a complete representation —
        this endpoint does not support partial updates; omitted fields are removed.

        Args:
            id: The `id` of the Destination to update.
            destination: Complete Destination configuration as a typed Output model or dict.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the updated Destination.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): The requested resource does not exist — Destination not found.
            ServerError (500): Unexpected server error.
        """
        body = destination.model_dump(exclude_none=True) if hasattr(destination, "model_dump") else dict(destination) # pyright: ignore[reportAttributeAccessIssue]
        body["id"] = id
        return self._patch(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[DestinationResponse], json=body)

    async def update_async(
        self,
        id: str,
        destination: Output | dict[str, object],
        *,
        pack: str | None = None,
    ) -> SDKResponse[PaginatedResponse[DestinationResponse]]:
        """Update a Destination (async).

        Update the specified Destination. Provide a complete representation —
        this endpoint does not support partial updates; omitted fields are removed.

        Args:
            id: The `id` of the Destination to update.
            destination: Complete Destination configuration as a typed Output model or dict.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the updated Destination.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): The requested resource does not exist — Destination not found.
            ServerError (500): Unexpected server error.
        """
        body = destination.model_dump(exclude_none=True) if hasattr(destination, "model_dump") else dict(destination) # pyright: ignore[reportAttributeAccessIssue]
        body["id"] = id
        return await self._patch_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[DestinationResponse], json=body)

    def delete(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[DestinationResponse]]:
        """Delete a Destination.

        Delete the specified Destination.

        Args:
            id: The `id` of the Destination to delete.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the deleted Destination.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): The requested resource does not exist — Destination not found.
            ServerError (500): Unexpected server error.
        """
        return self._delete(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[DestinationResponse])

    async def delete_async(self, id: str, *, pack: str | None = None) -> SDKResponse[PaginatedResponse[DestinationResponse]]:
        """Delete a Destination (async).

        Delete the specified Destination.

        Args:
            id: The `id` of the Destination to delete.
            pack: Pack ID. If provided, scopes the operation to the specified Pack.

        Returns:
            (200) PaginatedResponse containing the deleted Destination.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): The requested resource does not exist — Destination not found.
            ServerError (500): Unexpected server error.
        """
        return await self._delete_async(f"{self._base(pack)}/{id}", cast_to=PaginatedResponse[DestinationResponse])
