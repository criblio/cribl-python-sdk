"""Datasets resource (Cribl Lake)."""
from __future__ import annotations

from typing import Any, List

from .._response import SDKResponse
from ..models import (
    CacheConnectionParam,
    CriblLakeDataset,
    DatasetMetricsParam,
    DatasetSearchConfigParam,
    PaginatedResponse,
)
from ._base import BaseResource



class DatasetsResource(BaseResource):
    """Manage Cribl Lake Datasets."""

    def _path(self, lakeId: str) -> str:
        return f"/products/lake/lakes/{lakeId}/datasets"

    def list(
        self,
        lakeId: str,
        *,
        storageLocationId: str | None = None,
        format: str | None = None,
        excludeDDSS: bool | None = None,
        excludeNetskope: bool | None = None,
        excludeDeleted: bool | None = None,
        excludeInternal: bool | None = None,
        excludeBYOS: bool | None = None,
        includeMetrics: bool | None = None,
        offset: int | None = None,
        limit: int | None = None,
        orderBy: str | None = None,
        orderDir: str | None = None,
        name: str | None = None,
        nameContains: str | None = None,
        providerPathContains: str | None = None,
        descriptionContains: str | None = None,
    ) -> SDKResponse[PaginatedResponse[CriblLakeDataset]]:
        """List all Lake Datasets (Cribl.Cloud only).

        Get a list of all Lake Datasets in the specified Lake (Cribl.Cloud only).

        Args:
            lakeId: The `id` of the Lake that contains the Lake Datasets to
                list.
            storageLocationId: Filter datasets by storage location ID. Use
                `default` for default storage location.
            format: Filter datasets by format. Set to `ddss` to return only DDSS
                datasets.
            excludeDDSS: Exclude DDSS format datasets from the response.
            excludeNetskope: Exclude Netskope format datasets from the response.
            excludeDeleted: Exclude deleted datasets from the response.
            excludeInternal: Exclude internal datasets (those with IDs starting
                with `cribl_`) from the response.
            excludeBYOS: Exclude BYOS (Bring Your Own Storage) datasets from the
                response.
            includeMetrics: Set to `true` to include storage metrics for each
                Lake Dataset. Otherwise, `false` (default). Requires a Cribl
                Lake metrics license.
            offset: Starting point for catalog-backed pagination. Requires
                `limit`.
            limit: Page size for catalog-backed pagination. Requires `offset`.
            orderBy: Catalog sort field when paginating: `name`, `createdAt`,
                `updatedAt`, `providerPath`, `type`, or
                `retentionPeriodInDays`. Defaults to `name`.
            orderDir: Sort direction when paginating: `asc` or `desc`. Defaults
                to `asc`.
            name: Exact dataset name match (catalog path, with pagination).
            nameContains: Case-insensitive substring match on dataset name
                (catalog path, with pagination).
            providerPathContains: Case-insensitive substring match on provider
                path (catalog path, with pagination).
            descriptionContains: Case-insensitive substring match on description
                (catalog path, with pagination).

        Returns:
            (200) PaginatedResponse containing a list of CriblLakeDataset objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if storageLocationId is not None:
            params["storageLocationId"] = storageLocationId
        if format is not None:
            params["format"] = format
        if excludeDDSS is not None:
            params["excludeDDSS"] = excludeDDSS
        if excludeNetskope is not None:
            params["excludeNetskope"] = excludeNetskope
        if excludeDeleted is not None:
            params["excludeDeleted"] = excludeDeleted
        if excludeInternal is not None:
            params["excludeInternal"] = excludeInternal
        if excludeBYOS is not None:
            params["excludeBYOS"] = excludeBYOS
        if includeMetrics is not None:
            params["includeMetrics"] = includeMetrics
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        if orderBy is not None:
            params["orderBy"] = orderBy
        if orderDir is not None:
            params["orderDir"] = orderDir
        if name is not None:
            params["name"] = name
        if nameContains is not None:
            params["nameContains"] = nameContains
        if providerPathContains is not None:
            params["providerPathContains"] = providerPathContains
        if descriptionContains is not None:
            params["descriptionContains"] = descriptionContains
        return self._get(self._path(lakeId), cast_to=PaginatedResponse[CriblLakeDataset], params=params or None)

    async def list_async(
        self,
        lakeId: str,
        *,
        storageLocationId: str | None = None,
        format: str | None = None,
        excludeDDSS: bool | None = None,
        excludeNetskope: bool | None = None,
        excludeDeleted: bool | None = None,
        excludeInternal: bool | None = None,
        excludeBYOS: bool | None = None,
        includeMetrics: bool | None = None,
        offset: int | None = None,
        limit: int | None = None,
        orderBy: str | None = None,
        orderDir: str | None = None,
        name: str | None = None,
        nameContains: str | None = None,
        providerPathContains: str | None = None,
        descriptionContains: str | None = None,
    ) -> SDKResponse[PaginatedResponse[CriblLakeDataset]]:
        """List all Lake Datasets (Cribl.Cloud only) (async).

        Get a list of all Lake Datasets in the specified Lake (Cribl.Cloud only).

        Args:
            lakeId: The `id` of the Lake that contains the Lake Datasets to
                list.
            storageLocationId: Filter datasets by storage location ID. Use
                `default` for default storage location.
            format: Filter datasets by format. Set to `ddss` to return only DDSS
                datasets.
            excludeDDSS: Exclude DDSS format datasets from the response.
            excludeNetskope: Exclude Netskope format datasets from the response.
            excludeDeleted: Exclude deleted datasets from the response.
            excludeInternal: Exclude internal datasets (those with IDs starting
                with `cribl_`) from the response.
            excludeBYOS: Exclude BYOS (Bring Your Own Storage) datasets from the
                response.
            includeMetrics: Set to `true` to include storage metrics for each
                Lake Dataset. Otherwise, `false` (default). Requires a Cribl
                Lake metrics license.
            offset: Starting point for catalog-backed pagination. Requires
                `limit`.
            limit: Page size for catalog-backed pagination. Requires `offset`.
            orderBy: Catalog sort field when paginating: `name`, `createdAt`,
                `updatedAt`, `providerPath`, `type`, or
                `retentionPeriodInDays`. Defaults to `name`.
            orderDir: Sort direction when paginating: `asc` or `desc`. Defaults
                to `asc`.
            name: Exact dataset name match (catalog path, with pagination).
            nameContains: Case-insensitive substring match on dataset name
                (catalog path, with pagination).
            providerPathContains: Case-insensitive substring match on provider
                path (catalog path, with pagination).
            descriptionContains: Case-insensitive substring match on description
                (catalog path, with pagination).

        Returns:
            (200) PaginatedResponse containing a list of CriblLakeDataset objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if storageLocationId is not None:
            params["storageLocationId"] = storageLocationId
        if format is not None:
            params["format"] = format
        if excludeDDSS is not None:
            params["excludeDDSS"] = excludeDDSS
        if excludeNetskope is not None:
            params["excludeNetskope"] = excludeNetskope
        if excludeDeleted is not None:
            params["excludeDeleted"] = excludeDeleted
        if excludeInternal is not None:
            params["excludeInternal"] = excludeInternal
        if excludeBYOS is not None:
            params["excludeBYOS"] = excludeBYOS
        if includeMetrics is not None:
            params["includeMetrics"] = includeMetrics
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        if orderBy is not None:
            params["orderBy"] = orderBy
        if orderDir is not None:
            params["orderDir"] = orderDir
        if name is not None:
            params["name"] = name
        if nameContains is not None:
            params["nameContains"] = nameContains
        if providerPathContains is not None:
            params["providerPathContains"] = providerPathContains
        if descriptionContains is not None:
            params["descriptionContains"] = descriptionContains
        return await self._get_async(self._path(lakeId), cast_to=PaginatedResponse[CriblLakeDataset], params=params or None)

    def create(
        self,
        lakeId: str,
        *,
        id: str,
        acceleratedFields: List[str] | None = None,
        allowRecordErasure: bool | None = None,
        bucketName: str | None = None,
        cacheConnection: CacheConnectionParam | None = None,
        deletionStartedAt: int | None = None,
        description: str | None = None,
        format: str | None = None,
        httpDAUsed: bool | None = None,
        metrics: DatasetMetricsParam | None = None,
        providerPath: str | None = None,
        retentionPeriodInDays: int | None = None,
        searchConfig: DatasetSearchConfigParam | None = None,
        storageClass: str | None = None,
        storageLocationId: str | None = None,
        viewName: str | None = None,
    ) -> SDKResponse[PaginatedResponse[CriblLakeDataset]]:
        """Create Lake Datasets (Cribl.Cloud only).

        Creates one or more Lake Datasets in the specified Lake in a single
        transaction (Cribl.Cloud only). Send a single Lake Dataset object to
        create just one, or an array to bulk-create multiple. When an array is
        sent, the response is `{ items, errors }` -- `items` contains the
        successfully created Lake Datasets, and `errors` contains an entry
        (`{ id, reason }`) for each Lake Dataset that failed validation, so a
        per-item failure does not fail the rest of the batch.

        Args:
            lakeId: The `id` of the Lake to create the Lake Datasets in.
            id: Unique identifier for the Dataset.
            acceleratedFields: Accelerated fields for the Dataset. Data is
                partitioned by these fields in storage to improve query
                performance.
            allowRecordErasure: If `true`, the Dataset is opted in to Lake
                Record Erasure.
            bucketName: Name of the legacy Cribl Lake bucket that backs the
                Dataset. Mutually exclusive with `storageLocationId`.
            cacheConnection: Lakehouse cache connection settings for the
                Dataset.
            deletionStartedAt: Timestamp (in Unix time) when Dataset deletion
                was initiated, in milliseconds.
            description: Brief description of the Dataset.
            format: Storage format used for data persisted in the Dataset.
            httpDAUsed: If `true`, the Dataset is used by Direct Access HTTP.
                Otherwise, `false`.
            metrics: Most recent Dataset metrics snapshot.
            providerPath: Storage path within the provider (for example an S3
                prefix or Azure container).
            retentionPeriodInDays: Dataset retention period, in days.
            searchConfig: Search configuration for the Dataset.
            storageClass: Storage class used for objects written to the
                Dataset.
            storageLocationId: Unique identifier for the Storage Location
                that backs the Dataset. Mutually exclusive with `bucketName`.
            viewName: Name of the ClickHouse view for the Dataset on the
                Lakehouse.

        Returns:
            (200) PaginatedResponse containing the created CriblLakeDataset.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id}
        if acceleratedFields is not None:
            body["acceleratedFields"] = acceleratedFields
        if allowRecordErasure is not None:
            body["allowRecordErasure"] = allowRecordErasure
        if bucketName is not None:
            body["bucketName"] = bucketName
        if cacheConnection is not None:
            body["cacheConnection"] = cacheConnection
        if deletionStartedAt is not None:
            body["deletionStartedAt"] = deletionStartedAt
        if description is not None:
            body["description"] = description
        if format is not None:
            body["format"] = format
        if httpDAUsed is not None:
            body["httpDAUsed"] = httpDAUsed
        if metrics is not None:
            body["metrics"] = metrics
        if providerPath is not None:
            body["providerPath"] = providerPath
        if retentionPeriodInDays is not None:
            body["retentionPeriodInDays"] = retentionPeriodInDays
        if searchConfig is not None:
            body["searchConfig"] = searchConfig
        if storageClass is not None:
            body["storageClass"] = storageClass
        if storageLocationId is not None:
            body["storageLocationId"] = storageLocationId
        if viewName is not None:
            body["viewName"] = viewName
        return self._post(self._path(lakeId), cast_to=PaginatedResponse[CriblLakeDataset], json=body)

    async def create_async(
        self,
        lakeId: str,
        *,
        id: str,
        acceleratedFields: List[str] | None = None,
        allowRecordErasure: bool | None = None,
        bucketName: str | None = None,
        cacheConnection: CacheConnectionParam | None = None,
        deletionStartedAt: int | None = None,
        description: str | None = None,
        format: str | None = None,
        httpDAUsed: bool | None = None,
        metrics: DatasetMetricsParam | None = None,
        providerPath: str | None = None,
        retentionPeriodInDays: int | None = None,
        searchConfig: DatasetSearchConfigParam | None = None,
        storageClass: str | None = None,
        storageLocationId: str | None = None,
        viewName: str | None = None,
    ) -> SDKResponse[PaginatedResponse[CriblLakeDataset]]:
        """Create Lake Datasets (Cribl.Cloud only) (async).

        Creates one or more Lake Datasets in the specified Lake in a single
        transaction (Cribl.Cloud only). Send a single Lake Dataset object to
        create just one, or an array to bulk-create multiple. When an array is
        sent, the response is `{ items, errors }` -- `items` contains the
        successfully created Lake Datasets, and `errors` contains an entry
        (`{ id, reason }`) for each Lake Dataset that failed validation, so a
        per-item failure does not fail the rest of the batch.

        Args:
            lakeId: The `id` of the Lake to create the Lake Datasets in.
            id: Unique identifier for the Dataset.
            acceleratedFields: Accelerated fields for the Dataset. Data is
                partitioned by these fields in storage to improve query
                performance.
            allowRecordErasure: If `true`, the Dataset is opted in to Lake
                Record Erasure.
            bucketName: Name of the legacy Cribl Lake bucket that backs the
                Dataset. Mutually exclusive with `storageLocationId`.
            cacheConnection: Lakehouse cache connection settings for the
                Dataset.
            deletionStartedAt: Timestamp (in Unix time) when Dataset deletion
                was initiated, in milliseconds.
            description: Brief description of the Dataset.
            format: Storage format used for data persisted in the Dataset.
            httpDAUsed: If `true`, the Dataset is used by Direct Access HTTP.
                Otherwise, `false`.
            metrics: Most recent Dataset metrics snapshot.
            providerPath: Storage path within the provider (for example an S3
                prefix or Azure container).
            retentionPeriodInDays: Dataset retention period, in days.
            searchConfig: Search configuration for the Dataset.
            storageClass: Storage class used for objects written to the
                Dataset.
            storageLocationId: Unique identifier for the Storage Location
                that backs the Dataset. Mutually exclusive with `bucketName`.
            viewName: Name of the ClickHouse view for the Dataset on the
                Lakehouse.

        Returns:
            (200) PaginatedResponse containing the created CriblLakeDataset.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id}
        if acceleratedFields is not None:
            body["acceleratedFields"] = acceleratedFields
        if allowRecordErasure is not None:
            body["allowRecordErasure"] = allowRecordErasure
        if bucketName is not None:
            body["bucketName"] = bucketName
        if cacheConnection is not None:
            body["cacheConnection"] = cacheConnection
        if deletionStartedAt is not None:
            body["deletionStartedAt"] = deletionStartedAt
        if description is not None:
            body["description"] = description
        if format is not None:
            body["format"] = format
        if httpDAUsed is not None:
            body["httpDAUsed"] = httpDAUsed
        if metrics is not None:
            body["metrics"] = metrics
        if providerPath is not None:
            body["providerPath"] = providerPath
        if retentionPeriodInDays is not None:
            body["retentionPeriodInDays"] = retentionPeriodInDays
        if searchConfig is not None:
            body["searchConfig"] = searchConfig
        if storageClass is not None:
            body["storageClass"] = storageClass
        if storageLocationId is not None:
            body["storageLocationId"] = storageLocationId
        if viewName is not None:
            body["viewName"] = viewName
        return await self._post_async(self._path(lakeId), cast_to=PaginatedResponse[CriblLakeDataset], json=body)

    def get(self, lakeId: str, id: str, *, includeMetrics: bool | None = None) -> SDKResponse[PaginatedResponse[CriblLakeDataset]]:
        """Get a Lake Dataset (Cribl.Cloud only).

        Get the specified Lake Dataset in the specified Lake (Cribl.Cloud only).

        Args:
            lakeId: The `id` of the Lake that contains the Lake Dataset to get.
            id: The `id` of the Lake Dataset to get.
            includeMetrics: Set to `true` to include storage metrics for each
                Lake Dataset. Otherwise, `false` (default). Requires a Cribl
                Lake metrics license.

        Returns:
            (200) PaginatedResponse containing the requested CriblLakeDataset.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if includeMetrics is not None:
            params["includeMetrics"] = includeMetrics
        return self._get(f"{self._path(lakeId)}/{id}", cast_to=PaginatedResponse[CriblLakeDataset], params=params or None)

    async def get_async(self, lakeId: str, id: str, *, includeMetrics: bool | None = None) -> SDKResponse[PaginatedResponse[CriblLakeDataset]]:
        """Get a Lake Dataset (Cribl.Cloud only) (async).

        Get the specified Lake Dataset in the specified Lake (Cribl.Cloud only).

        Args:
            lakeId: The `id` of the Lake that contains the Lake Dataset to get.
            id: The `id` of the Lake Dataset to get.
            includeMetrics: Set to `true` to include storage metrics for each
                Lake Dataset. Otherwise, `false` (default). Requires a Cribl
                Lake metrics license.

        Returns:
            (200) PaginatedResponse containing the requested CriblLakeDataset.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if includeMetrics is not None:
            params["includeMetrics"] = includeMetrics
        return await self._get_async(f"{self._path(lakeId)}/{id}", cast_to=PaginatedResponse[CriblLakeDataset], params=params or None)

    def update(
        self,
        lakeId: str,
        id: str,
        *,
        acceleratedFields: List[str] | None = None,
        allowRecordErasure: bool | None = None,
        bucketName: str | None = None,
        cacheConnection: CacheConnectionParam | None = None,
        deletionStartedAt: int | None = None,
        description: str | None = None,
        format: str | None = None,
        httpDAUsed: bool | None = None,
        metrics: DatasetMetricsParam | None = None,
        providerPath: str | None = None,
        retentionPeriodInDays: int | None = None,
        searchConfig: DatasetSearchConfigParam | None = None,
        storageClass: str | None = None,
        storageLocationId: str | None = None,
        viewName: str | None = None,
    ) -> SDKResponse[PaginatedResponse[CriblLakeDataset]]:
        """Update a Lake Dataset (Cribl.Cloud only).

        Update the specified Lake Dataset in the specified Lake (Cribl.Cloud
        only).

        Args:
            lakeId: The `id` of the Lake that contains the Lake Dataset to
                update.
            id: The `id` of the Lake Dataset to update.
            acceleratedFields: Accelerated fields for the Dataset. Data is
                partitioned by these fields in storage to improve query
                performance.
            allowRecordErasure: If `true`, the Dataset is opted in to Lake
                Record Erasure.
            bucketName: Name of the legacy Cribl Lake bucket that backs the
                Dataset. Mutually exclusive with `storageLocationId`.
            cacheConnection: Lakehouse cache connection settings for the
                Dataset.
            deletionStartedAt: Timestamp (in Unix time) when Dataset deletion
                was initiated, in milliseconds.
            description: Brief description of the Dataset.
            format: Storage format used for data persisted in the Dataset.
            httpDAUsed: If `true`, the Dataset is used by Direct Access HTTP.
                Otherwise, `false`.
            metrics: Most recent Dataset metrics snapshot.
            providerPath: Storage path within the provider (for example an S3
                prefix or Azure container).
            retentionPeriodInDays: Dataset retention period, in days.
            searchConfig: Search configuration for the Dataset.
            storageClass: Storage class used for objects written to the
                Dataset.
            storageLocationId: Unique identifier for the Storage Location
                that backs the Dataset. Mutually exclusive with `bucketName`.
            viewName: Name of the ClickHouse view for the Dataset on the
                Lakehouse.

        Returns:
            (200) PaginatedResponse containing the updated CriblLakeDataset.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {}
        if acceleratedFields is not None:
            body["acceleratedFields"] = acceleratedFields
        if allowRecordErasure is not None:
            body["allowRecordErasure"] = allowRecordErasure
        if bucketName is not None:
            body["bucketName"] = bucketName
        if cacheConnection is not None:
            body["cacheConnection"] = cacheConnection
        if deletionStartedAt is not None:
            body["deletionStartedAt"] = deletionStartedAt
        if description is not None:
            body["description"] = description
        if format is not None:
            body["format"] = format
        if httpDAUsed is not None:
            body["httpDAUsed"] = httpDAUsed
        if metrics is not None:
            body["metrics"] = metrics
        if providerPath is not None:
            body["providerPath"] = providerPath
        if retentionPeriodInDays is not None:
            body["retentionPeriodInDays"] = retentionPeriodInDays
        if searchConfig is not None:
            body["searchConfig"] = searchConfig
        if storageClass is not None:
            body["storageClass"] = storageClass
        if storageLocationId is not None:
            body["storageLocationId"] = storageLocationId
        if viewName is not None:
            body["viewName"] = viewName
        return self._patch(f"{self._path(lakeId)}/{id}", cast_to=PaginatedResponse[CriblLakeDataset], json=body)

    async def update_async(
        self,
        lakeId: str,
        id: str,
        *,
        acceleratedFields: List[str] | None = None,
        allowRecordErasure: bool | None = None,
        bucketName: str | None = None,
        cacheConnection: CacheConnectionParam | None = None,
        deletionStartedAt: int | None = None,
        description: str | None = None,
        format: str | None = None,
        httpDAUsed: bool | None = None,
        metrics: DatasetMetricsParam | None = None,
        providerPath: str | None = None,
        retentionPeriodInDays: int | None = None,
        searchConfig: DatasetSearchConfigParam | None = None,
        storageClass: str | None = None,
        storageLocationId: str | None = None,
        viewName: str | None = None,
    ) -> SDKResponse[PaginatedResponse[CriblLakeDataset]]:
        """Update a Lake Dataset (Cribl.Cloud only) (async).

        Update the specified Lake Dataset in the specified Lake (Cribl.Cloud
        only).

        Args:
            lakeId: The `id` of the Lake that contains the Lake Dataset to
                update.
            id: The `id` of the Lake Dataset to update.
            acceleratedFields: Accelerated fields for the Dataset. Data is
                partitioned by these fields in storage to improve query
                performance.
            allowRecordErasure: If `true`, the Dataset is opted in to Lake
                Record Erasure.
            bucketName: Name of the legacy Cribl Lake bucket that backs the
                Dataset. Mutually exclusive with `storageLocationId`.
            cacheConnection: Lakehouse cache connection settings for the
                Dataset.
            deletionStartedAt: Timestamp (in Unix time) when Dataset deletion
                was initiated, in milliseconds.
            description: Brief description of the Dataset.
            format: Storage format used for data persisted in the Dataset.
            httpDAUsed: If `true`, the Dataset is used by Direct Access HTTP.
                Otherwise, `false`.
            metrics: Most recent Dataset metrics snapshot.
            providerPath: Storage path within the provider (for example an S3
                prefix or Azure container).
            retentionPeriodInDays: Dataset retention period, in days.
            searchConfig: Search configuration for the Dataset.
            storageClass: Storage class used for objects written to the
                Dataset.
            storageLocationId: Unique identifier for the Storage Location
                that backs the Dataset. Mutually exclusive with `bucketName`.
            viewName: Name of the ClickHouse view for the Dataset on the
                Lakehouse.

        Returns:
            (200) PaginatedResponse containing the updated CriblLakeDataset.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {}
        if acceleratedFields is not None:
            body["acceleratedFields"] = acceleratedFields
        if allowRecordErasure is not None:
            body["allowRecordErasure"] = allowRecordErasure
        if bucketName is not None:
            body["bucketName"] = bucketName
        if cacheConnection is not None:
            body["cacheConnection"] = cacheConnection
        if deletionStartedAt is not None:
            body["deletionStartedAt"] = deletionStartedAt
        if description is not None:
            body["description"] = description
        if format is not None:
            body["format"] = format
        if httpDAUsed is not None:
            body["httpDAUsed"] = httpDAUsed
        if metrics is not None:
            body["metrics"] = metrics
        if providerPath is not None:
            body["providerPath"] = providerPath
        if retentionPeriodInDays is not None:
            body["retentionPeriodInDays"] = retentionPeriodInDays
        if searchConfig is not None:
            body["searchConfig"] = searchConfig
        if storageClass is not None:
            body["storageClass"] = storageClass
        if storageLocationId is not None:
            body["storageLocationId"] = storageLocationId
        if viewName is not None:
            body["viewName"] = viewName
        return await self._patch_async(f"{self._path(lakeId)}/{id}", cast_to=PaginatedResponse[CriblLakeDataset], json=body)

    def delete(self, lakeId: str, id: str) -> SDKResponse[PaginatedResponse[CriblLakeDataset]]:
        """Delete a Lake Dataset (Cribl.Cloud only).

        Delete the specified Lake Dataset in the specified Lake (Cribl.Cloud
        only).

        Args:
            lakeId: The `id` of the Lake that contains the Lake Dataset to
                delete.
            id: The `id` of the Lake Dataset to delete.

        Returns:
            (200) PaginatedResponse containing the deleted CriblLakeDataset.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._delete(f"{self._path(lakeId)}/{id}", cast_to=PaginatedResponse[CriblLakeDataset])

    async def delete_async(self, lakeId: str, id: str) -> SDKResponse[PaginatedResponse[CriblLakeDataset]]:
        """Delete a Lake Dataset (Cribl.Cloud only) (async).

        Delete the specified Lake Dataset in the specified Lake (Cribl.Cloud
        only).

        Args:
            lakeId: The `id` of the Lake that contains the Lake Dataset to
                delete.
            id: The `id` of the Lake Dataset to delete.

        Returns:
            (200) PaginatedResponse containing the deleted CriblLakeDataset.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._delete_async(f"{self._path(lakeId)}/{id}", cast_to=PaginatedResponse[CriblLakeDataset])
