"""Groups resource."""
from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Any, Literal, List
from warnings import deprecated

from .._response import SDKResponse
from ..models import CloudParam, ConfigGroup, ConfigGroupLookups, DeployRequestLookupsParam, EstimatedIngestRate, GitStatusParam, PaginatedResponse, TeamAccessControlList, UserAccessControlList
from ._base import BaseResource

if TYPE_CHECKING:
    from ..client import Cribl



def _groups_path(product: str) -> str:
    return f"/products/{product}/groups"


class GroupsAclTeamsResource(BaseResource):
    """Team ACL operations (`groups.acl.teams`)."""

    def get(
        self,
        id: str,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        type: Literal["groups", "insights-apps", "datasets", "dataset-providers", "projects", "dashboards", "macros", "notebooks", "notebook-templates", "apps"] | None = None,
    ) -> SDKResponse[PaginatedResponse[TeamAccessControlList]]:
        """Get the team access control list for a Worker Group, Outpost Group, or Edge Fleet.

        Get the Team access control list (ACL) for the specified Worker Group,
        Outpost Group, or Edge Fleet.

        This endpoint lists Teams with explicit access assignments on the Group
        or Fleet. The response does not include access granted to individual
        Team Members through direct user assignments or inherited based on Team
        Permissions and Roles at the Organization/Global, Workspace, or product
        level.

        To list the user ACL for a Group or Fleet, use
        `GET /products/{product}/groups/{id}/acl`.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to get the Team ACL for.
            product: Name of the Cribl product that contains the Worker Group, Outpost Group, or Edge Fleet. Valid values: "stream", "edge", "outpost". Default: "stream".
            type: Filter for limiting the response to ACL entries for the specified RBAC resource type. Valid values: "groups", "insights-apps", "datasets", "dataset-providers", "projects", "dashboards", "macros", "notebooks", "notebook-templates", "apps".

        Returns:
            (200) PaginatedResponse containing a list of TeamAccessControlList objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if type is not None:
            params["type"] = type
        return self._get(f"{_groups_path(product)}/{id}/acl/teams", cast_to=PaginatedResponse[TeamAccessControlList], params=params or None)

    async def get_async(
        self,
        id: str,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        type: Literal["groups", "insights-apps", "datasets", "dataset-providers", "projects", "dashboards", "macros", "notebooks", "notebook-templates", "apps"] | None = None,
    ) -> SDKResponse[PaginatedResponse[TeamAccessControlList]]:
        """Get the team access control list for a Worker Group, Outpost Group, or Edge Fleet (async).

        Get the Team access control list (ACL) for the specified Worker Group,
        Outpost Group, or Edge Fleet.

        This endpoint lists Teams with explicit access assignments on the Group
        or Fleet. The response does not include access granted to individual
        Team Members through direct user assignments or inherited based on Team
        Permissions and Roles at the Organization/Global, Workspace, or product
        level.

        To list the user ACL for a Group or Fleet, use
        `GET /products/{product}/groups/{id}/acl`.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to get the Team ACL for.
            product: Name of the Cribl product that contains the Worker Group, Outpost Group, or Edge Fleet. Valid values: "stream", "edge", "outpost". Default: "stream".
            type: Filter for limiting the response to ACL entries for the specified RBAC resource type. Valid values: "groups", "insights-apps", "datasets", "dataset-providers", "projects", "dashboards", "macros", "notebooks", "notebook-templates", "apps".

        Returns:
            (200) PaginatedResponse containing a list of TeamAccessControlList objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if type is not None:
            params["type"] = type
        return await self._get_async(f"{_groups_path(product)}/{id}/acl/teams", cast_to=PaginatedResponse[TeamAccessControlList], params=params or None)


class GroupsAclResource(BaseResource):
    """ACL operations for Groups (`groups.acl`)."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.teams = GroupsAclTeamsResource(client)

    def get(
        self,
        id: str,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        type: Literal["groups", "insights-apps", "datasets", "dataset-providers", "projects", "dashboards", "macros", "notebooks", "notebook-templates", "apps"] | None = None,
    ) -> SDKResponse[PaginatedResponse[UserAccessControlList]]:
        """Get the user access control list for a Worker Group, Outpost Group, or Edge Fleet.

        Get the user access control list (ACL) for the specified Worker Group,
        Outpost Group, or Edge Fleet.

        This endpoint lists users with explicit access assignments on the Group
        or Fleet. The response does not include access granted through Team
        membership or inherited based on a user's Permissions and Roles at the
        Organization/Global, Workspace, or product level.

        To list the Team ACL for a product and Group or Fleet, use
        `GET /products/{product}/groups/{id}/acl/teams`.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to
                get the ACL for.
            product: Name of the Cribl product that contains the Worker Group, Outpost Group, or Edge Fleet. Valid values: "stream", "edge", "outpost". Default: "stream".
            type: Filter for limiting the response to ACL entries for the
                specified RBAC resource type. Valid values: "groups",
                "insights-apps", "datasets", "dataset-providers", "projects",
                "dashboards", "macros", "notebooks", "notebook-templates", "apps".

        Returns:
            (200) PaginatedResponse containing a list of UserAccessControlList objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Worker Group, Outpost Group, or Edge Fleet not found.
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if type is not None:
            params["type"] = type
        return self._get(f"{_groups_path(product)}/{id}/acl", cast_to=PaginatedResponse[UserAccessControlList], params=params or None)

    async def get_async(
        self,
        id: str,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        type: Literal["groups", "insights-apps", "datasets", "dataset-providers", "projects", "dashboards", "macros", "notebooks", "notebook-templates", "apps"] | None = None,
    ) -> SDKResponse[PaginatedResponse[UserAccessControlList]]:
        """Get the user access control list for a Worker Group, Outpost Group, or Edge Fleet (async).

        Get the user access control list (ACL) for the specified Worker Group,
        Outpost Group, or Edge Fleet.

        This endpoint lists users with explicit access assignments on the Group
        or Fleet. The response does not include access granted through Team
        membership or inherited based on a user's Permissions and Roles at the
        Organization/Global, Workspace, or product level.

        To list the Team ACL for a product and Group or Fleet, use
        `GET /products/{product}/groups/{id}/acl/teams`.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to
                get the ACL for.
            product: Name of the Cribl product that contains the Worker Group, Outpost Group, or Edge Fleet. Valid values: "stream", "edge", "outpost". Default: "stream".
            type: Filter for limiting the response to ACL entries for the
                specified RBAC resource type. Valid values: "groups",
                "insights-apps", "datasets", "dataset-providers", "projects",
                "dashboards", "macros", "notebooks", "notebook-templates", "apps".

        Returns:
            (200) PaginatedResponse containing a list of UserAccessControlList objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Worker Group, Outpost Group, or Edge Fleet not found.
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if type is not None:
            params["type"] = type
        return await self._get_async(f"{_groups_path(product)}/{id}/acl", cast_to=PaginatedResponse[UserAccessControlList], params=params or None)


class GroupsConfigsVersionsResource(BaseResource):
    """Config version operations (`groups.configs.versions`)."""

    def get(self, id: str, *, product: Literal["stream", "edge", "outpost"] = "stream") -> SDKResponse[PaginatedResponse[str]]:
        """Get the configuration version for a Worker Group, Outpost Group, or Edge Fleet.

        Get the configuration version for the specified Worker Group, Outpost
        Group, or Edge Fleet.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to
                get the configuration version for.
            product: Name of the Cribl product to get the Worker Groups, Outpost Groups, or Edge Fleets for. Valid values: "stream", "edge", "outpost". Default: "stream".

        Returns:
            (200) PaginatedResponse containing the requested str.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(f"{_groups_path(product)}/{id}/configVersion", cast_to=PaginatedResponse[str])

    async def get_async(self, id: str, *, product: Literal["stream", "edge", "outpost"] = "stream") -> SDKResponse[PaginatedResponse[str]]:
        """Get the configuration version for a Worker Group, Outpost Group, or Edge Fleet (async).

        Get the configuration version for the specified Worker Group, Outpost
        Group, or Edge Fleet.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to
                get the configuration version for.
            product: Name of the Cribl product to get the Worker Groups, Outpost Groups, or Edge Fleets for. Valid values: "stream", "edge", "outpost". Default: "stream".

        Returns:
            (200) PaginatedResponse containing the requested str.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"{_groups_path(product)}/{id}/configVersion", cast_to=PaginatedResponse[str])


class GroupsConfigsResource(BaseResource):
    """Config sub-resource for Groups (`groups.configs`)."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.versions = GroupsConfigsVersionsResource(client)


class GroupsResource(BaseResource):
    """Manage Worker Groups, Outpost Groups, and Edge Fleets."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.acl = GroupsAclResource(client)
        self.configs = GroupsConfigsResource(client)

    def _path(self, product: str) -> str:
        return _groups_path(product)

    def list(
        self,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        fields: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """List all Worker Groups, Outpost Groups, or Edge Fleets.

        Get a list of all Worker Groups, Outpost Groups, or Edge Fleets for the
        specified Cribl product.

        Args:
            product: Name of the Cribl product to get the Worker Groups, Outpost Groups, or Edge Fleets for. Valid values: "stream", "edge", "outpost". Default: "stream".
            fields: Comma-separated list of additional properties to include in
                the response. Available values are `git.commit`,
                `git.localChanges`, and `git.log`.
            offset: Starting point from which to retrieve results for this
                request. Use with `limit` to paginate the response into
                manageable batches.
            limit: Maximum number of Worker Groups, Outpost Groups, or Edge
                Fleets to return in the response for this request. Use with
                `offset` to paginate the response into manageable batches.

        Returns:
            (200) PaginatedResponse containing a list of ConfigGroup objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if fields is not None:
            params["fields"] = fields
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get(self._path(product), cast_to=PaginatedResponse[ConfigGroup], params=params or None)

    async def list_async(
        self,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        fields: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """List all Worker Groups, Outpost Groups, or Edge Fleets (async).

        Get a list of all Worker Groups, Outpost Groups, or Edge Fleets for the
        specified Cribl product.

        Args:
            product: Name of the Cribl product to get the Worker Groups, Outpost Groups, or Edge Fleets for. Valid values: "stream", "edge", "outpost". Default: "stream".
            fields: Comma-separated list of additional properties to include in
                the response. Available values are `git.commit`,
                `git.localChanges`, and `git.log`.
            offset: Starting point from which to retrieve results for this
                request. Use with `limit` to paginate the response into
                manageable batches.
            limit: Maximum number of Worker Groups, Outpost Groups, or Edge
                Fleets to return in the response for this request. Use with
                `offset` to paginate the response into manageable batches.

        Returns:
            (200) PaginatedResponse containing a list of ConfigGroup objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if fields is not None:
            params["fields"] = fields
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return await self._get_async(self._path(product), cast_to=PaginatedResponse[ConfigGroup], params=params or None)

    def create(
        self,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        id: str,
        cloud: CloudParam | None = None,
        collectorsHaEnabled: bool | None = None,
        description: str | None = None,
        estimatedIngestRate: EstimatedIngestRate | int | None = None,
        inherits: str | None = None,
        isFleet: Annotated[bool | None, deprecated("Use type='edge' instead")] = None,
        isSearch: Annotated[bool | None, deprecated("Use type='search' instead")] = None,
        maxWorkerAge: str | None = None,
        name: str | None = None,
        onPrem: bool | None = None,
        provisioned: bool | None = None,
        sourceGroupId: str | None = None,
        streamtags: List[str] | None = None,
        tags: Annotated[str | None, deprecated("Use streamtags instead")] = None,
        type: Literal["edge", "lake_access", "local_search", "outpost", "search", "stream"] | None = None,
        upgradeVersion: str | None = None,
        workerRemoteAccess: bool | None = None,
    ) -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """Create a Worker Group, Outpost Group, or Edge Fleet.

        Create a new Worker Group, Outpost Group, or Edge Fleet for the
        specified Cribl product.

        Args:
            product: Name of the Cribl product to add the Worker Group, Outpost Group, or Edge Fleet to. Valid values: "stream", "edge", "outpost". Default: "stream".
            id: Unique identifier.
            cloud: Cloud provider and region details for a Cribl.Cloud Worker
                Group.
            collectorsHaEnabled: Keeps Collector jobs running if the Leader
                Node fails. Applies only to Stream Worker Groups. Always
                `true` for Cribl.Cloud groups; defaults to `false` for
                on-prem groups.
            description: Brief description of the Worker Group, Outpost
                Group, or Edge Fleet.
            estimatedIngestRate: Estimated ingest rate for a Cribl.Cloud
                Worker Group, in GB/sec.
            inherits: The `id` of the parent Edge Fleet. If provided, this
                Fleet inherits configuration from the specified parent Fleet.
                Applies only to Edge Fleets.
            isFleet: Indicates whether this is an Edge Fleet. Deprecated.
            isSearch: Indicates whether this is an internal Search Group.
                Deprecated.
            maxWorkerAge: Maximum duration a Worker or Node can remain
                disconnected before the Leader removes it.
            name: Name of the Worker Group, Outpost Group, or Edge Fleet.
            onPrem: If `true`, the Group or Fleet uses customer-hosted
                (on-prem) workers. If `false`, managed in Cribl.Cloud.
            provisioned: If `true`, the Cribl.Cloud Worker Group has active
                Workers provisioned.
            sourceGroupId: The `id` of an existing Group or Fleet to copy
                configuration from when creating a new Group or Fleet.
            streamtags: Metadata tags for categorization, filtering, and
                tag-based routing and policy application.
            tags: Legacy system-level tags. Use `streamtags` instead.
            type: Explicit type of the Worker Group, Outpost Group, or Edge Fleet.
                Valid values: "edge", "lake_access", "local_search", "outpost", "search", "stream".
            upgradeVersion: Target software upgrade version. Applies only to
                Outpost Groups and Edge Fleets.
            workerRemoteAccess: If `true`, the Leader allows remote access
                (teleporting) into the Workers or Nodes.

        Returns:
            (200) PaginatedResponse containing the created ConfigGroup.

        Raises:
            ValidationError (400): Failed validation or malformed input -- Invalid group payload or invalid cloud/on-prem configuration.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id}
        if cloud is not None:
            body["cloud"] = cloud
        if collectorsHaEnabled is not None:
            body["collectorsHaEnabled"] = collectorsHaEnabled
        if description is not None:
            body["description"] = description
        if estimatedIngestRate is not None:
            body["estimatedIngestRate"] = estimatedIngestRate
        if inherits is not None:
            body["inherits"] = inherits
        if isFleet is not None:
            body["isFleet"] = isFleet
        if isSearch is not None:
            body["isSearch"] = isSearch
        if maxWorkerAge is not None:
            body["maxWorkerAge"] = maxWorkerAge
        if name is not None:
            body["name"] = name
        if onPrem is not None:
            body["onPrem"] = onPrem
        if provisioned is not None:
            body["provisioned"] = provisioned
        if sourceGroupId is not None:
            body["sourceGroupId"] = sourceGroupId
        if streamtags is not None:
            body["streamtags"] = streamtags
        if tags is not None:
            body["tags"] = tags
        if type is not None:
            body["type"] = type
        if upgradeVersion is not None:
            body["upgradeVersion"] = upgradeVersion
        if workerRemoteAccess is not None:
            body["workerRemoteAccess"] = workerRemoteAccess
        return self._post(self._path(product), cast_to=PaginatedResponse[ConfigGroup], json=body)

    async def create_async(
        self,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        id: str,
        cloud: CloudParam | None = None,
        collectorsHaEnabled: bool | None = None,
        description: str | None = None,
        estimatedIngestRate: EstimatedIngestRate | int | None = None,
        inherits: str | None = None,
        isFleet: Annotated[bool | None, deprecated("Use type='edge' instead")] = None,
        isSearch: Annotated[bool | None, deprecated("Use type='search' instead")] = None,
        maxWorkerAge: str | None = None,
        name: str | None = None,
        onPrem: bool | None = None,
        provisioned: bool | None = None,
        sourceGroupId: str | None = None,
        streamtags: List[str] | None = None,
        tags: Annotated[str | None, deprecated("Use streamtags instead")] = None,
        type: Literal["edge", "lake_access", "local_search", "outpost", "search", "stream"] | None = None,
        upgradeVersion: str | None = None,
        workerRemoteAccess: bool | None = None,
    ) -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """Create a Worker Group, Outpost Group, or Edge Fleet (async).

        Create a new Worker Group, Outpost Group, or Edge Fleet for the
        specified Cribl product.

        Args:
            product: Name of the Cribl product to add the Worker Group, Outpost Group, or Edge Fleet to. Valid values: "stream", "edge", "outpost". Default: "stream".
            id: Unique identifier.
            cloud: Cloud provider and region details for a Cribl.Cloud Worker
                Group.
            collectorsHaEnabled: Keeps Collector jobs running if the Leader
                Node fails. Applies only to Stream Worker Groups. Always
                `true` for Cribl.Cloud groups; defaults to `false` for
                on-prem groups.
            description: Brief description of the Worker Group, Outpost
                Group, or Edge Fleet.
            estimatedIngestRate: Estimated ingest rate for a Cribl.Cloud
                Worker Group, in GB/sec.
            inherits: The `id` of the parent Edge Fleet. If provided, this
                Fleet inherits configuration from the specified parent Fleet.
                Applies only to Edge Fleets.
            isFleet: Indicates whether this is an Edge Fleet. Deprecated.
            isSearch: Indicates whether this is an internal Search Group.
                Deprecated.
            maxWorkerAge: Maximum duration a Worker or Node can remain
                disconnected before the Leader removes it.
            name: Name of the Worker Group, Outpost Group, or Edge Fleet.
            onPrem: If `true`, the Group or Fleet uses customer-hosted
                (on-prem) workers. If `false`, managed in Cribl.Cloud.
            provisioned: If `true`, the Cribl.Cloud Worker Group has active
                Workers provisioned.
            sourceGroupId: The `id` of an existing Group or Fleet to copy
                configuration from when creating a new Group or Fleet.
            streamtags: Metadata tags for categorization, filtering, and
                tag-based routing and policy application.
            tags: Legacy system-level tags. Use `streamtags` instead.
            type: Explicit type of the Worker Group, Outpost Group, or Edge Fleet.
                Valid values: "edge", "lake_access", "local_search", "outpost", "search", "stream".
            upgradeVersion: Target software upgrade version. Applies only to
                Outpost Groups and Edge Fleets.
            workerRemoteAccess: If `true`, the Leader allows remote access
                (teleporting) into the Workers or Nodes.

        Returns:
            (200) PaginatedResponse containing the created ConfigGroup.

        Raises:
            ValidationError (400): Failed validation or malformed input -- Invalid group payload or invalid cloud/on-prem configuration.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id}
        if cloud is not None:
            body["cloud"] = cloud
        if collectorsHaEnabled is not None:
            body["collectorsHaEnabled"] = collectorsHaEnabled
        if description is not None:
            body["description"] = description
        if estimatedIngestRate is not None:
            body["estimatedIngestRate"] = estimatedIngestRate
        if inherits is not None:
            body["inherits"] = inherits
        if isFleet is not None:
            body["isFleet"] = isFleet
        if isSearch is not None:
            body["isSearch"] = isSearch
        if maxWorkerAge is not None:
            body["maxWorkerAge"] = maxWorkerAge
        if name is not None:
            body["name"] = name
        if onPrem is not None:
            body["onPrem"] = onPrem
        if provisioned is not None:
            body["provisioned"] = provisioned
        if sourceGroupId is not None:
            body["sourceGroupId"] = sourceGroupId
        if streamtags is not None:
            body["streamtags"] = streamtags
        if tags is not None:
            body["tags"] = tags
        if type is not None:
            body["type"] = type
        if upgradeVersion is not None:
            body["upgradeVersion"] = upgradeVersion
        if workerRemoteAccess is not None:
            body["workerRemoteAccess"] = workerRemoteAccess
        return await self._post_async(self._path(product), cast_to=PaginatedResponse[ConfigGroup], json=body)

    def get(self, id: str, *, product: Literal["stream", "edge", "outpost"] = "stream", fields: str | None = None) -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """Get a Worker Group, Outpost Group, or Edge Fleet.

        Get the specified Worker Group, Outpost Group, or Edge Fleet.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to
                get.
            product: Name of the Cribl product to get the Worker Groups, Outpost Groups, or Edge Fleets for. Valid values: "stream", "edge", "outpost". Default: "stream".
            fields: Comma-separated list of additional properties to include in
                the response. Available values are `git.commit`,
                `git.localChanges`, and `git.log`.

        Returns:
            (200) PaginatedResponse containing the requested ConfigGroup.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Worker Group, Outpost Group, or Edge Fleet not found.
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if fields is not None:
            params["fields"] = fields
        return self._get(f"{self._path(product)}/{id}", cast_to=PaginatedResponse[ConfigGroup], params=params or None)

    async def get_async(self, id: str, *, product: Literal["stream", "edge", "outpost"] = "stream", fields: str | None = None) -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """Get a Worker Group, Outpost Group, or Edge Fleet (async).

        Get the specified Worker Group, Outpost Group, or Edge Fleet.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to
                get.
            product: Name of the Cribl product to get the Worker Groups, Outpost Groups, or Edge Fleets for. Valid values: "stream", "edge", "outpost". Default: "stream".
            fields: Comma-separated list of additional properties to include in
                the response. Available values are `git.commit`,
                `git.localChanges`, and `git.log`.

        Returns:
            (200) PaginatedResponse containing the requested ConfigGroup.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Worker Group, Outpost Group, or Edge Fleet not found.
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if fields is not None:
            params["fields"] = fields
        return await self._get_async(f"{self._path(product)}/{id}", cast_to=PaginatedResponse[ConfigGroup], params=params or None)

    def update(
        self,
        id: str,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        cloud: CloudParam | None = None,
        collectorsHaEnabled: bool | None = None,
        configVersion: str | None = None,
        deployingWorkerCount: int | None = None,
        description: str | None = None,
        estimatedIngestRate: EstimatedIngestRate | int | None = None,
        git: GitStatusParam | None = None,
        incompatibleWorkerCount: int | None = None,
        inherits: str | None = None,
        isFleet: Annotated[bool | None, deprecated("Use type='edge' instead")] = None,
        isSearch: Annotated[bool | None, deprecated("Use type='search' instead")] = None,
        lookupDeployments: List[ConfigGroupLookups] | None = None,
        maxWorkerAge: str | None = None,
        name: str | None = None,
        onPrem: bool | None = None,
        provisioned: bool | None = None,
        streamtags: List[str] | None = None,
        tags: Annotated[str | None, deprecated("Use streamtags instead")] = None,
        type: Literal["edge", "lake_access", "local_search", "outpost", "search", "stream"] | None = None,
        upgradeVersion: str | None = None,
        workerCount: int | None = None,
        workerRemoteAccess: bool | None = None,
    ) -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """Update a Worker Group, Outpost Group, or Edge Fleet.

        Update the specified Worker Group, Outpost Group, or Edge Fleet.

        Provide a complete representation of the Group or Fleet that you want to
        update in the request body. This endpoint does not support partial
        updates. Cribl removes any omitted fields when updating the Group or
        Fleet.

        Confirm that the configuration in your request body is correct before
        sending the request. If the configuration is incorrect, the updated
        Group or Fleet might not function as expected.

        Warning: Do not change the values for the following parameters in the
        body of PATCH requests. The request body must include the values as they
        appear in the GET response: `configVersion`, `deployingWorkerCount`,
        `incompatibleWorkerCount`, `workerCount`, `lookupDeployments`.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to
                update.
            product: Name of the Cribl product that contains the Worker Group,
                Outpost Group, or Edge Fleet. Valid values: "stream", "edge",
                "outpost". Default: "stream".
            cloud: Cloud provider and region details for a Cribl.Cloud Worker
                Group.
            collectorsHaEnabled: Keeps Collector jobs running if the Leader
                Node fails. Applies only to Stream Worker Groups.
            configVersion: Commit hash of the deployed configuration version.
                Do not change in PATCH requests.
            deployingWorkerCount: Number of Workers currently deploying. Do
                not change in PATCH requests.
            description: Brief description of the Worker Group, Outpost
                Group, or Edge Fleet.
            estimatedIngestRate: Estimated ingest rate for a Cribl.Cloud
                Worker Group, in GB/sec.
            git: Git status of the configuration. Automatically populated.
            incompatibleWorkerCount: Number of Workers running an
                incompatible Cribl version. Do not change in PATCH requests.
            inherits: The `id` of the parent Edge Fleet.
            isFleet: Indicates whether this is an Edge Fleet. Deprecated.
            isSearch: Indicates whether this is an internal Search Group.
                Deprecated.
            lookupDeployments: Lookup deployment status per Worker or Node
                context. Do not change in PATCH requests.
            maxWorkerAge: Maximum duration a Worker or Node can remain
                disconnected before the Leader removes it.
            name: Name of the Worker Group, Outpost Group, or Edge Fleet.
            onPrem: If `true`, uses customer-hosted (on-prem) workers.
            provisioned: If `true`, the Cribl.Cloud Worker Group has active
                Workers provisioned.
            streamtags: Metadata tags for categorization, filtering, and
                tag-based routing and policy application.
            tags: Legacy system-level tags. Use `streamtags` instead.
            type: Explicit type of the Worker Group, Outpost Group, or Edge Fleet.
                Valid values: "edge", "lake_access", "local_search", "outpost", "search", "stream".
            upgradeVersion: Target software upgrade version.
            workerCount: Number of Workers or Nodes. Do not change in PATCH
                requests.
            workerRemoteAccess: If `true`, the Leader allows remote access
                (teleporting) into the Workers or Nodes.

        Returns:
            (200) PaginatedResponse containing the updated ConfigGroup.

        Raises:
            ValidationError (400): Failed validation or malformed input -- Invalid update payload, including read-only field mutations or invalid cloud/on-prem configuration.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id}
        if cloud is not None:
            body["cloud"] = cloud
        if collectorsHaEnabled is not None:
            body["collectorsHaEnabled"] = collectorsHaEnabled
        if configVersion is not None:
            body["configVersion"] = configVersion
        if deployingWorkerCount is not None:
            body["deployingWorkerCount"] = deployingWorkerCount
        if description is not None:
            body["description"] = description
        if estimatedIngestRate is not None:
            body["estimatedIngestRate"] = estimatedIngestRate
        if git is not None:
            body["git"] = git
        if incompatibleWorkerCount is not None:
            body["incompatibleWorkerCount"] = incompatibleWorkerCount
        if inherits is not None:
            body["inherits"] = inherits
        if isFleet is not None:
            body["isFleet"] = isFleet
        if isSearch is not None:
            body["isSearch"] = isSearch
        if lookupDeployments is not None:
            body["lookupDeployments"] = lookupDeployments
        if maxWorkerAge is not None:
            body["maxWorkerAge"] = maxWorkerAge
        if name is not None:
            body["name"] = name
        if onPrem is not None:
            body["onPrem"] = onPrem
        if provisioned is not None:
            body["provisioned"] = provisioned
        if streamtags is not None:
            body["streamtags"] = streamtags
        if tags is not None:
            body["tags"] = tags
        if type is not None:
            body["type"] = type
        if upgradeVersion is not None:
            body["upgradeVersion"] = upgradeVersion
        if workerCount is not None:
            body["workerCount"] = workerCount
        if workerRemoteAccess is not None:
            body["workerRemoteAccess"] = workerRemoteAccess
        return self._patch(f"{self._path(product)}/{id}", cast_to=PaginatedResponse[ConfigGroup], json=body)

    async def update_async(
        self,
        id: str,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        cloud: CloudParam | None = None,
        collectorsHaEnabled: bool | None = None,
        configVersion: str | None = None,
        deployingWorkerCount: int | None = None,
        description: str | None = None,
        estimatedIngestRate: EstimatedIngestRate | int | None = None,
        git: GitStatusParam | None = None,
        incompatibleWorkerCount: int | None = None,
        inherits: str | None = None,
        isFleet: Annotated[bool | None, deprecated("Use type='edge' instead")] = None,
        isSearch: Annotated[bool | None, deprecated("Use type='search' instead")] = None,
        lookupDeployments: List[ConfigGroupLookups] | None = None,
        maxWorkerAge: str | None = None,
        name: str | None = None,
        onPrem: bool | None = None,
        provisioned: bool | None = None,
        streamtags: List[str] | None = None,
        tags: Annotated[str | None, deprecated("Use streamtags instead")] = None,
        type: Literal["edge", "lake_access", "local_search", "outpost", "search", "stream"] | None = None,
        upgradeVersion: str | None = None,
        workerCount: int | None = None,
        workerRemoteAccess: bool | None = None,
    ) -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """Update a Worker Group, Outpost Group, or Edge Fleet (async).

        Update the specified Worker Group, Outpost Group, or Edge Fleet.

        Provide a complete representation of the Group or Fleet that you want to
        update in the request body. This endpoint does not support partial
        updates. Cribl removes any omitted fields when updating the Group or
        Fleet.

        Confirm that the configuration in your request body is correct before
        sending the request. If the configuration is incorrect, the updated
        Group or Fleet might not function as expected.

        Warning: Do not change the values for the following parameters in the
        body of PATCH requests. The request body must include the values as they
        appear in the GET response: `configVersion`, `deployingWorkerCount`,
        `incompatibleWorkerCount`, `workerCount`, `lookupDeployments`.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to
                update.
            product: Name of the Cribl product that contains the Worker Group,
                Outpost Group, or Edge Fleet. Valid values: "stream", "edge",
                "outpost". Default: "stream".
            cloud: Cloud provider and region details for a Cribl.Cloud Worker
                Group.
            collectorsHaEnabled: Keeps Collector jobs running if the Leader
                Node fails. Applies only to Stream Worker Groups.
            configVersion: Commit hash of the deployed configuration version.
                Do not change in PATCH requests.
            deployingWorkerCount: Number of Workers currently deploying. Do
                not change in PATCH requests.
            description: Brief description of the Worker Group, Outpost
                Group, or Edge Fleet.
            estimatedIngestRate: Estimated ingest rate for a Cribl.Cloud
                Worker Group, in GB/sec.
            git: Git status of the configuration. Automatically populated.
            incompatibleWorkerCount: Number of Workers running an
                incompatible Cribl version. Do not change in PATCH requests.
            inherits: The `id` of the parent Edge Fleet.
            isFleet: Indicates whether this is an Edge Fleet. Deprecated.
            isSearch: Indicates whether this is an internal Search Group.
                Deprecated.
            lookupDeployments: Lookup deployment status per Worker or Node
                context. Do not change in PATCH requests.
            maxWorkerAge: Maximum duration a Worker or Node can remain
                disconnected before the Leader removes it.
            name: Name of the Worker Group, Outpost Group, or Edge Fleet.
            onPrem: If `true`, uses customer-hosted (on-prem) workers.
            provisioned: If `true`, the Cribl.Cloud Worker Group has active
                Workers provisioned.
            streamtags: Metadata tags for categorization, filtering, and
                tag-based routing and policy application.
            tags: Legacy system-level tags. Use `streamtags` instead.
            type: Explicit type of the Worker Group, Outpost Group, or Edge Fleet.
                Valid values: "edge", "lake_access", "local_search", "outpost", "search", "stream".
            upgradeVersion: Target software upgrade version.
            workerCount: Number of Workers or Nodes. Do not change in PATCH
                requests.
            workerRemoteAccess: If `true`, the Leader allows remote access
                (teleporting) into the Workers or Nodes.

        Returns:
            (200) PaginatedResponse containing the updated ConfigGroup.

        Raises:
            ValidationError (400): Failed validation or malformed input -- Invalid update payload, including read-only field mutations or invalid cloud/on-prem configuration.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"id": id}
        if cloud is not None:
            body["cloud"] = cloud
        if collectorsHaEnabled is not None:
            body["collectorsHaEnabled"] = collectorsHaEnabled
        if configVersion is not None:
            body["configVersion"] = configVersion
        if deployingWorkerCount is not None:
            body["deployingWorkerCount"] = deployingWorkerCount
        if description is not None:
            body["description"] = description
        if estimatedIngestRate is not None:
            body["estimatedIngestRate"] = estimatedIngestRate
        if git is not None:
            body["git"] = git
        if incompatibleWorkerCount is not None:
            body["incompatibleWorkerCount"] = incompatibleWorkerCount
        if inherits is not None:
            body["inherits"] = inherits
        if isFleet is not None:
            body["isFleet"] = isFleet
        if isSearch is not None:
            body["isSearch"] = isSearch
        if lookupDeployments is not None:
            body["lookupDeployments"] = lookupDeployments
        if maxWorkerAge is not None:
            body["maxWorkerAge"] = maxWorkerAge
        if name is not None:
            body["name"] = name
        if onPrem is not None:
            body["onPrem"] = onPrem
        if provisioned is not None:
            body["provisioned"] = provisioned
        if streamtags is not None:
            body["streamtags"] = streamtags
        if tags is not None:
            body["tags"] = tags
        if type is not None:
            body["type"] = type
        if upgradeVersion is not None:
            body["upgradeVersion"] = upgradeVersion
        if workerCount is not None:
            body["workerCount"] = workerCount
        if workerRemoteAccess is not None:
            body["workerRemoteAccess"] = workerRemoteAccess
        return await self._patch_async(f"{self._path(product)}/{id}", cast_to=PaginatedResponse[ConfigGroup], json=body)

    def delete(self, id: str, *, product: Literal["stream", "edge", "outpost"] = "stream") -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """Delete a Worker Group, Outpost Group, or Edge Fleet.

        Delete the specified Worker Group, Outpost Group, or Edge Fleet.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to
                delete.
            product: Name of the Cribl product that contains the Worker Group,
                Outpost Group, or Edge Fleet. Valid values: "stream", "edge",
                "outpost". Default: "stream".

        Returns:
            (200) PaginatedResponse containing the deleted ConfigGroup.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._delete(f"{self._path(product)}/{id}", cast_to=PaginatedResponse[ConfigGroup])

    async def delete_async(self, id: str, *, product: Literal["stream", "edge", "outpost"] = "stream") -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """Delete a Worker Group, Outpost Group, or Edge Fleet (async).

        Delete the specified Worker Group, Outpost Group, or Edge Fleet.

        Args:
            id: The `id` of the Worker Group, Outpost Group, or Edge Fleet to
                delete.
            product: Name of the Cribl product that contains the Worker Group,
                Outpost Group, or Edge Fleet. Valid values: "stream", "edge",
                "outpost". Default: "stream".

        Returns:
            (200) PaginatedResponse containing the deleted ConfigGroup.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._delete_async(f"{self._path(product)}/{id}", cast_to=PaginatedResponse[ConfigGroup])

    def deploy(
        self,
        id: str,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        version: str,
        lookups: List[DeployRequestLookupsParam] | None = None,
    ) -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """Deploy commits to a Worker Group, Outpost Group, or Edge Fleet.

        Deploy commits to the specified Worker Group, Outpost Group, or Edge
        Fleet.

        Args:
            id: The `id` of the target Worker Group, Outpost Group, or Edge
                Fleet for commit deployment.
            product: Name of the Cribl product that contains the Worker Group, Outpost Group, or Edge Fleet. Valid values: "stream", "edge", "outpost". Default: "stream".
            version: Commit hash to deploy to the Worker Group, Outpost Group,
                or Edge Fleet.
            lookups: Optional list of lookup file deployments to include with the
                commit deployment.

        Returns:
            (200) PaginatedResponse containing the deployment result.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"version": version}
        if lookups is not None:
            body["lookups"] = lookups
        return self._patch(f"{self._path(product)}/{id}/deploy", cast_to=PaginatedResponse[ConfigGroup], json=body)

    async def deploy_async(
        self,
        id: str,
        *,
        product: Literal["stream", "edge", "outpost"] = "stream",
        version: str,
        lookups: List[DeployRequestLookupsParam] | None = None,
    ) -> SDKResponse[PaginatedResponse[ConfigGroup]]:
        """Deploy commits to a Worker Group, Outpost Group, or Edge Fleet (async).

        Deploy commits to the specified Worker Group, Outpost Group, or Edge
        Fleet.

        Args:
            id: The `id` of the target Worker Group, Outpost Group, or Edge
                Fleet for commit deployment.
            product: Name of the Cribl product that contains the Worker Group, Outpost Group, or Edge Fleet. Valid values: "stream", "edge", "outpost". Default: "stream".
            version: Commit hash to deploy to the Worker Group, Outpost Group,
                or Edge Fleet.
            lookups: Optional list of lookup file deployments to include with the
                commit deployment.

        Returns:
            (200) PaginatedResponse containing the deployment result.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"version": version}
        if lookups is not None:
            body["lookups"] = lookups
        return await self._patch_async(f"{self._path(product)}/{id}/deploy", cast_to=PaginatedResponse[ConfigGroup], json=body)
