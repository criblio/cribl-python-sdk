"""Cribl.Cloud platform (mgmt) resources — `client.cloud.*`."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List

from .._response import SDKResponse
from .._unset import UNSET, Nullable, _UnsetType
from ..models import (
    ApiCredentialCreateResponseSchema,
    ApiCredentialResponseSchema,
    ApiCredentialRolesParam,
    ApiCredentialsListResponseDTO,
    BillingWindow,
    CloudHealthStatus,
    ContractsUtilizationResponseDTO,
    CreditGrantsResponseDTO,
    CreditsStatsResponseDTO,
    CreditsTimeseriesResponseDTO,
    WorkspaceSchema,
    WorkspacesListResponseDTO,
)
from ._base import BaseResource

if TYPE_CHECKING:
    from ..client import Cribl



def _omit_unset(body: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in body.items() if not isinstance(v, _UnsetType)}


class CloudHealthResource(BaseResource):
    """Cribl.Cloud platform health (`cloud.health`)."""

    _surface = "cloud"

    def get(self) -> SDKResponse[CloudHealthStatus]:
        """Get the health status of the application.

        Returns:
            (200) CloudHealthStatus with gateway health information.

        Raises:
            ServerError (500): Unexpected server error.
        """
        return self._get("/", cast_to=CloudHealthStatus)

    async def get_async(self) -> SDKResponse[CloudHealthStatus]:
        """Get the health status of the application (async).

        Returns:
            (200) CloudHealthStatus with gateway health information.

        Raises:
            ServerError (500): Unexpected server error.
        """
        return await self._get_async("/", cast_to=CloudHealthStatus)


class CloudApiCredentialsResource(BaseResource):
    """API Credentials for a Cribl.Cloud Organization (`cloud.api_credentials`)."""

    _surface = "cloud"

    def _path(self, organization_id: str, api_credential_id: str | None = None) -> str:
        base = f"/v1/organizations/{organization_id}/api-credentials"
        if api_credential_id is None:
            return base
        return f"{base}/{api_credential_id}"

    def list(self, organization_id: str) -> SDKResponse[ApiCredentialsListResponseDTO]:
        """List API Credentials for an Organization.

        Get a list of all API Credentials for the specified Organization.

        Args:
            organization_id: The id of the Organization whose API Credentials you want to list.

        Returns:
            (200) ApiCredentialsListResponseDTO containing a list of API Credentials.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(self._path(organization_id), cast_to=ApiCredentialsListResponseDTO)

    async def list_async(self, organization_id: str) -> SDKResponse[ApiCredentialsListResponseDTO]:
        """List API Credentials for an Organization (async).

        Get a list of all API Credentials for the specified Organization.

        Args:
            organization_id: The id of the Organization whose API Credentials you want to list.

        Returns:
            (200) ApiCredentialsListResponseDTO containing a list of API Credentials.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(self._path(organization_id), cast_to=ApiCredentialsListResponseDTO)

    def create(
        self,
        organization_id: str,
        *,
        name: str,
        description: str,
        enabled: bool,
        roles: ApiCredentialRolesParam,
        ipAllowlist: List[str] | None = None,
    ) -> SDKResponse[ApiCredentialCreateResponseSchema]:
        """Create an API Credential.

        Create a new API Credential for the specified Organization.

        Args:
            organization_id: The id of the Organization where you want to create the API Credential.
            name: Human-readable name of the API Credential.
            description: Brief description of the purpose and usage for the API Credential.
            enabled: If true, the API Credential is enabled. Otherwise, false.
            roles: Role assignments for the API Credential.
            ipAllowlist: CIDR range enforced as the IP allowlist for the API Credential.

        Returns:
            (201) ApiCredentialCreateResponseSchema containing the created API Credential (includes clientSecret).

        Raises:
            ValidationError (409): Could not create API Credential because it already exists.
            ValidationError (422): API Credential limit reached.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {
            "name": name,
            "description": description,
            "enabled": enabled,
            "roles": roles,
        }
        if ipAllowlist is not None:
            body["ipAllowlist"] = ipAllowlist
        return self._post(self._path(organization_id), cast_to=ApiCredentialCreateResponseSchema, json=body)

    async def create_async(
        self,
        organization_id: str,
        *,
        name: str,
        description: str,
        enabled: bool,
        roles: ApiCredentialRolesParam,
        ipAllowlist: List[str] | None = None,
    ) -> SDKResponse[ApiCredentialCreateResponseSchema]:
        """Create an API Credential (async).

        Create a new API Credential for the specified Organization.

        Args:
            organization_id: The id of the Organization where you want to create the API Credential.
            name: Human-readable name of the API Credential.
            description: Brief description of the purpose and usage for the API Credential.
            enabled: If true, the API Credential is enabled. Otherwise, false.
            roles: Role assignments for the API Credential.
            ipAllowlist: CIDR range enforced as the IP allowlist for the API Credential.

        Returns:
            (201) ApiCredentialCreateResponseSchema containing the created API Credential (includes clientSecret).

        Raises:
            ValidationError (409): Could not create API Credential because it already exists.
            ValidationError (422): API Credential limit reached.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {
            "name": name,
            "description": description,
            "enabled": enabled,
            "roles": roles,
        }
        if ipAllowlist is not None:
            body["ipAllowlist"] = ipAllowlist
        return await self._post_async(self._path(organization_id), cast_to=ApiCredentialCreateResponseSchema, json=body)

    def get(self, organization_id: str, api_credential_id: str) -> SDKResponse[ApiCredentialResponseSchema]:
        """Get an API Credential.

        Get the specified API Credential.

        Args:
            organization_id: The id of the Organization whose API Credential you want to retrieve.
            api_credential_id: The clientId of the API Credential to retrieve.

        Returns:
            (200) ApiCredentialResponseSchema for the requested API Credential.

        Raises:
            NotFoundError (404): API Credential not found.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(self._path(organization_id, api_credential_id), cast_to=ApiCredentialResponseSchema)

    async def get_async(self, organization_id: str, api_credential_id: str) -> SDKResponse[ApiCredentialResponseSchema]:
        """Get an API Credential (async).

        Get the specified API Credential.

        Args:
            organization_id: The id of the Organization whose API Credential you want to retrieve.
            api_credential_id: The clientId of the API Credential to retrieve.

        Returns:
            (200) ApiCredentialResponseSchema for the requested API Credential.

        Raises:
            NotFoundError (404): API Credential not found.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(self._path(organization_id, api_credential_id), cast_to=ApiCredentialResponseSchema)

    def update(
        self,
        organization_id: str,
        api_credential_id: str,
        *,
        name: Nullable[str] = UNSET,
        description: Nullable[str] = UNSET,
        enabled: Nullable[bool] = UNSET,
        roles: Nullable[ApiCredentialRolesParam] = UNSET,
        ipAllowlist: Nullable[List[str]] = UNSET,
    ) -> SDKResponse[None]:
        """Update an API Credential.

        Update the specified API Credential.

        Args:
            organization_id: The id of the Organization whose API Credential you want to update.
            api_credential_id: The clientId of the API Credential to update.
            name: Human-readable name of the API Credential.
            description: Brief description of the purpose and usage for the API Credential.
            enabled: If true, the API Credential is enabled. Otherwise, false.
            roles: Role assignments for the API Credential.
            ipAllowlist: Omit to leave unchanged. Pass an empty array to clear the stored IP allowlist.

        Returns:
            (204) Empty response when the API Credential is updated.

        Raises:
            NotFoundError (404): API Credential not found.
            ValidationError (409): Could not update API Credential because the name is already in use.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = _omit_unset({
            "name": name,
            "description": description,
            "enabled": enabled,
            "roles": roles,
            "ipAllowlist": ipAllowlist,
        })
        resp = self._client._request("PATCH", self._path(organization_id, api_credential_id), json=body, surface="cloud")
        return SDKResponse(data=None, status_code=resp.status_code, headers=resp.headers, raw_response=resp)

    async def update_async(
        self,
        organization_id: str,
        api_credential_id: str,
        *,
        name: Nullable[str] = UNSET,
        description: Nullable[str] = UNSET,
        enabled: Nullable[bool] = UNSET,
        roles: Nullable[ApiCredentialRolesParam] = UNSET,
        ipAllowlist: Nullable[List[str]] = UNSET,
    ) -> SDKResponse[None]:
        """Update an API Credential (async).

        Update the specified API Credential.

        Args:
            organization_id: The id of the Organization whose API Credential you want to update.
            api_credential_id: The clientId of the API Credential to update.
            name: Human-readable name of the API Credential.
            description: Brief description of the purpose and usage for the API Credential.
            enabled: If true, the API Credential is enabled. Otherwise, false.
            roles: Role assignments for the API Credential.
            ipAllowlist: Omit to leave unchanged. Pass an empty array to clear the stored IP allowlist.

        Returns:
            (204) Empty response when the API Credential is updated.

        Raises:
            NotFoundError (404): API Credential not found.
            ValidationError (409): Could not update API Credential because the name is already in use.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = _omit_unset({
            "name": name,
            "description": description,
            "enabled": enabled,
            "roles": roles,
            "ipAllowlist": ipAllowlist,
        })
        resp = await self._client._request_async("PATCH", self._path(organization_id, api_credential_id), json=body, surface="cloud")
        return SDKResponse(data=None, status_code=resp.status_code, headers=resp.headers, raw_response=resp)

    def delete(self, organization_id: str, api_credential_id: str) -> SDKResponse[None]:
        """Delete an API Credential.

        Delete the specified API Credential.

        Args:
            organization_id: The id of the Organization whose API Credential you want to delete.
            api_credential_id: The clientId of the API Credential to delete.

        Returns:
            (204) Empty response when the API Credential is deleted.

        Raises:
            NotFoundError (404): API Credential not found.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        resp = self._client._request("DELETE", self._path(organization_id, api_credential_id), surface="cloud")
        return SDKResponse(data=None, status_code=resp.status_code, headers=resp.headers, raw_response=resp)

    async def delete_async(self, organization_id: str, api_credential_id: str) -> SDKResponse[None]:
        """Delete an API Credential (async).

        Delete the specified API Credential.

        Args:
            organization_id: The id of the Organization whose API Credential you want to delete.
            api_credential_id: The clientId of the API Credential to delete.

        Returns:
            (204) Empty response when the API Credential is deleted.

        Raises:
            NotFoundError (404): API Credential not found.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        resp = await self._client._request_async("DELETE", self._path(organization_id, api_credential_id), surface="cloud")
        return SDKResponse(data=None, status_code=resp.status_code, headers=resp.headers, raw_response=resp)


class CloudWorkspacesResource(BaseResource):
    """Workspaces for a Cribl.Cloud Organization (`cloud.workspaces`)."""

    _surface = "cloud"

    def _path(self, organization_id: str, workspace_id: str | None = None) -> str:
        base = f"/v1/organizations/{organization_id}/workspaces"
        if workspace_id is None:
            return base
        return f"{base}/{workspace_id}"

    def list(self, organization_id: str) -> SDKResponse[WorkspacesListResponseDTO]:
        """List all Workspaces for the specified Organization.

        Get a list of all Workspaces for the specified Organization.

        Args:
            organization_id: The id of the Organization that contains the Workspaces.

        Returns:
            (200) WorkspacesListResponseDTO containing a list of Workspace objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(self._path(organization_id), cast_to=WorkspacesListResponseDTO)

    async def list_async(self, organization_id: str) -> SDKResponse[WorkspacesListResponseDTO]:
        """List all Workspaces for the specified Organization (async).

        Get a list of all Workspaces for the specified Organization.

        Args:
            organization_id: The id of the Organization that contains the Workspaces.

        Returns:
            (200) WorkspacesListResponseDTO containing a list of Workspace objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(self._path(organization_id), cast_to=WorkspacesListResponseDTO)

    def create(
        self,
        organization_id: str,
        *,
        workspaceId: str,
        alias: str | None = None,
        description: str | None = None,
        tags: List[str] | None = None,
    ) -> SDKResponse[WorkspaceSchema]:
        """Create a Workspace in the specified Organization.

        Create a new Workspace in the specified Organization.

        Args:
            organization_id: The id of the Organization where you want to create the Workspace.
            workspaceId: Unique identifier for the Workspace.
            alias: User-friendly alias for the Workspace.
            description: Brief description of the Workspace.
            tags: Tags associated with the Workspace.

        Returns:
            (201) WorkspaceSchema for the created Workspace.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"workspaceId": workspaceId}
        if alias is not None:
            body["alias"] = alias
        if description is not None:
            body["description"] = description
        if tags is not None:
            body["tags"] = tags
        return self._post(self._path(organization_id), cast_to=WorkspaceSchema, json=body)

    async def create_async(
        self,
        organization_id: str,
        *,
        workspaceId: str,
        alias: str | None = None,
        description: str | None = None,
        tags: List[str] | None = None,
    ) -> SDKResponse[WorkspaceSchema]:
        """Create a Workspace in the specified Organization (async).

        Create a new Workspace in the specified Organization.

        Args:
            organization_id: The id of the Organization where you want to create the Workspace.
            workspaceId: Unique identifier for the Workspace.
            alias: User-friendly alias for the Workspace.
            description: Brief description of the Workspace.
            tags: Tags associated with the Workspace.

        Returns:
            (201) WorkspaceSchema for the created Workspace.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"workspaceId": workspaceId}
        if alias is not None:
            body["alias"] = alias
        if description is not None:
            body["description"] = description
        if tags is not None:
            body["tags"] = tags
        return await self._post_async(self._path(organization_id), cast_to=WorkspaceSchema, json=body)

    def get(self, organization_id: str, workspace_id: str) -> SDKResponse[WorkspaceSchema]:
        """Get a Workspace.

        Args:
            organization_id: The id of the Organization that contains the Workspace.
            workspace_id: The id of the Workspace to retrieve.

        Returns:
            (200) WorkspaceSchema for the requested Workspace.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(self._path(organization_id, workspace_id), cast_to=WorkspaceSchema)

    async def get_async(self, organization_id: str, workspace_id: str) -> SDKResponse[WorkspaceSchema]:
        """Get a Workspace (async).

        Args:
            organization_id: The id of the Organization that contains the Workspace.
            workspace_id: The id of the Workspace to retrieve.

        Returns:
            (200) WorkspaceSchema for the requested Workspace.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(self._path(organization_id, workspace_id), cast_to=WorkspaceSchema)

    def update(
        self,
        organization_id: str,
        workspace_id: str,
        *,
        alias: Nullable[str] = UNSET,
        description: Nullable[str] = UNSET,
        tags: Nullable[List[str]] = UNSET,
    ) -> SDKResponse[None]:
        """Update a Workspace.

        Update the specified Workspace.

        Args:
            organization_id: The id of the Organization that contains the Workspace.
            workspace_id: The id of the Workspace to update.
            alias: User-friendly alias for the Workspace.
            description: Brief description of the Workspace.
            tags: Tags associated with the Workspace.

        Returns:
            (204) Empty response when the Workspace is updated.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = _omit_unset({"alias": alias, "description": description, "tags": tags})
        resp = self._client._request("PATCH", self._path(organization_id, workspace_id), json=body, surface="cloud")
        return SDKResponse(data=None, status_code=resp.status_code, headers=resp.headers, raw_response=resp)

    async def update_async(
        self,
        organization_id: str,
        workspace_id: str,
        *,
        alias: Nullable[str] = UNSET,
        description: Nullable[str] = UNSET,
        tags: Nullable[List[str]] = UNSET,
    ) -> SDKResponse[None]:
        """Update a Workspace (async).

        Update the specified Workspace.

        Args:
            organization_id: The id of the Organization that contains the Workspace.
            workspace_id: The id of the Workspace to update.
            alias: User-friendly alias for the Workspace.
            description: Brief description of the Workspace.
            tags: Tags associated with the Workspace.

        Returns:
            (204) Empty response when the Workspace is updated.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body = _omit_unset({"alias": alias, "description": description, "tags": tags})
        resp = await self._client._request_async("PATCH", self._path(organization_id, workspace_id), json=body, surface="cloud")
        return SDKResponse(data=None, status_code=resp.status_code, headers=resp.headers, raw_response=resp)

    def delete(self, organization_id: str, workspace_id: str) -> SDKResponse[None]:
        """Delete a Workspace.

        Args:
            organization_id: The id of the Organization that contains the Workspace.
            workspace_id: The id of the Workspace to delete.

        Returns:
            (204) Empty response when the Workspace is deleted.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        resp = self._client._request("DELETE", self._path(organization_id, workspace_id), surface="cloud")
        return SDKResponse(data=None, status_code=resp.status_code, headers=resp.headers, raw_response=resp)

    async def delete_async(self, organization_id: str, workspace_id: str) -> SDKResponse[None]:
        """Delete a Workspace (async).

        Args:
            organization_id: The id of the Organization that contains the Workspace.
            workspace_id: The id of the Workspace to delete.

        Returns:
            (204) Empty response when the Workspace is deleted.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        resp = await self._client._request_async("DELETE", self._path(organization_id, workspace_id), surface="cloud")
        return SDKResponse(data=None, status_code=resp.status_code, headers=resp.headers, raw_response=resp)


class CloudBillingCreditsContractsUtilizationResource(BaseResource):
    """Contract credit utilization (`cloud.billing.credits.contracts_utilization`)."""

    _surface = "cloud"

    def list(
        self,
        organization_id: str,
        *,
        startingOn: str,
        endingBefore: str,
        window: BillingWindow,
    ) -> SDKResponse[ContractsUtilizationResponseDTO]:
        """Get contract credit utilization.

        Get cumulative credit utilization data grouped by contract period for the specified Organization.

        Args:
            organization_id: The id of the Organization.
            startingOn: Inclusive start of the query date range in ISO 8601 format. Must be before endingBefore. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly.
            endingBefore: Exclusive end of the query date range in ISO 8601 format. Must be after startingOn. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly.
            window: Aggregation granularity for credit utilization data. Determines the maximum allowed date range: up to 6 months for daily, up to 7 years for monthly. Valid values: "monthly", "daily".

        Returns:
            (200) ContractsUtilizationResponseDTO with contract utilization data.

        Raises:
            ServerError (503): FinOps endpoints are in development with restricted availability. Contact Cribl Support to request access.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params = {"startingOn": startingOn, "endingBefore": endingBefore, "window": window}
        return self._get(
            f"/v1/organizations/{organization_id}/billing/credits/contracts-utilization",
            cast_to=ContractsUtilizationResponseDTO,
            params=params,
        )

    async def list_async(
        self,
        organization_id: str,
        *,
        startingOn: str,
        endingBefore: str,
        window: BillingWindow,
    ) -> SDKResponse[ContractsUtilizationResponseDTO]:
        """Get contract credit utilization (async).

        Get cumulative credit utilization data grouped by contract period for the specified Organization.

        Args:
            organization_id: The id of the Organization.
            startingOn: Inclusive start of the query date range in ISO 8601 format. Must be before endingBefore. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly.
            endingBefore: Exclusive end of the query date range in ISO 8601 format. Must be after startingOn. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly.
            window: Aggregation granularity for credit utilization data. Determines the maximum allowed date range: up to 6 months for daily, up to 7 years for monthly. Valid values: "monthly", "daily".

        Returns:
            (200) ContractsUtilizationResponseDTO with contract utilization data.

        Raises:
            ServerError (503): FinOps endpoints are in development with restricted availability. Contact Cribl Support to request access.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params = {"startingOn": startingOn, "endingBefore": endingBefore, "window": window}
        return await self._get_async(
            f"/v1/organizations/{organization_id}/billing/credits/contracts-utilization",
            cast_to=ContractsUtilizationResponseDTO,
            params=params,
        )


class CloudBillingCreditsTimeseriesResource(BaseResource):
    """Credit consumption timeseries (`cloud.billing.credits.timeseries`)."""

    _surface = "cloud"

    def list(
        self,
        organization_id: str,
        *,
        startingOn: str,
        endingBefore: str,
        window: BillingWindow,
    ) -> SDKResponse[CreditsTimeseriesResponseDTO]:
        """Get credits timeseries.

        Get credit consumption timeseries data for the specified Organization, broken down by dimensions such as product and usage type.

        Args:
            organization_id: The id of the Organization.
            startingOn: Inclusive start of the query date range in ISO 8601 format. Must be before endingBefore. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly.
            endingBefore: Exclusive end of the query date range in ISO 8601 format. Must be after startingOn. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly.
            window: Aggregation granularity for timeseries data. Determines the maximum allowed date range: up to 6 months for daily, up to 7 years for monthly. Valid values: "monthly", "daily".

        Returns:
            (200) CreditsTimeseriesResponseDTO with timeseries data points.

        Raises:
            ServerError (503): FinOps endpoints are in development with restricted availability. Contact Cribl Support to request access.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params = {"startingOn": startingOn, "endingBefore": endingBefore, "window": window}
        return self._get(
            f"/v1/organizations/{organization_id}/billing/credits/timeseries",
            cast_to=CreditsTimeseriesResponseDTO,
            params=params,
        )

    async def list_async(
        self,
        organization_id: str,
        *,
        startingOn: str,
        endingBefore: str,
        window: BillingWindow,
    ) -> SDKResponse[CreditsTimeseriesResponseDTO]:
        """Get credits timeseries (async).

        Get credit consumption timeseries data for the specified Organization, broken down by dimensions such as product and usage type.

        Args:
            organization_id: The id of the Organization.
            startingOn: Inclusive start of the query date range in ISO 8601 format. Must be before endingBefore. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly.
            endingBefore: Exclusive end of the query date range in ISO 8601 format. Must be after startingOn. Minimum range is 1 day. Maximum range depends on window: 6 months for daily, 7 years for monthly.
            window: Aggregation granularity for timeseries data. Determines the maximum allowed date range: up to 6 months for daily, up to 7 years for monthly. Valid values: "monthly", "daily".

        Returns:
            (200) CreditsTimeseriesResponseDTO with timeseries data points.

        Raises:
            ServerError (503): FinOps endpoints are in development with restricted availability. Contact Cribl Support to request access.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params = {"startingOn": startingOn, "endingBefore": endingBefore, "window": window}
        return await self._get_async(
            f"/v1/organizations/{organization_id}/billing/credits/timeseries",
            cast_to=CreditsTimeseriesResponseDTO,
            params=params,
        )


class CloudBillingCreditsStatsResource(BaseResource):
    """Credit balance and consumption totals (`cloud.billing.credits.stats`)."""

    _surface = "cloud"

    def list(
        self,
        organization_id: str,
    ) -> SDKResponse[CreditsStatsResponseDTO]:
        """Get credit balance and consumption.

        Get credit balance totals, consumption totals, and contract date ranges for the specified Organization.

        Args:
            organization_id: The id of the Organization.

        Returns:
            (200) CreditsStatsResponseDTO with credit balance and consumption totals.

        Raises:
            ServerError (503): FinOps endpoints are in development with restricted availability. Contact Cribl Support to request access.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(
            f"/v1/organizations/{organization_id}/billing/credits/stats",
            cast_to=CreditsStatsResponseDTO,
        )

    async def list_async(
        self,
        organization_id: str,
    ) -> SDKResponse[CreditsStatsResponseDTO]:
        """Get credit balance and consumption (async).

        Get credit balance totals, consumption totals, and contract date ranges for the specified Organization.

        Args:
            organization_id: The id of the Organization.

        Returns:
            (200) CreditsStatsResponseDTO with credit balance and consumption totals.

        Raises:
            ServerError (503): FinOps endpoints are in development with restricted availability. Contact Cribl Support to request access.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(
            f"/v1/organizations/{organization_id}/billing/credits/stats",
            cast_to=CreditsStatsResponseDTO,
        )


class CloudBillingCreditsGrantsResource(BaseResource):
    """Credit grants (`cloud.billing.credits.grants`)."""

    _surface = "cloud"

    def list(
        self,
        organization_id: str,
    ) -> SDKResponse[CreditGrantsResponseDTO]:
        """Get credit grants.

        Get credit grants (purchases, rollovers, and refunds) for the specified Organization.

        Args:
            organization_id: The id of the Organization.

        Returns:
            (200) CreditGrantsResponseDTO containing credit grants for the current contract.

        Raises:
            ServerError (503): FinOps endpoints are in development with restricted availability. Contact Cribl Support to request access.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(
            f"/v1/organizations/{organization_id}/billing/credits/grants",
            cast_to=CreditGrantsResponseDTO,
        )

    async def list_async(
        self,
        organization_id: str,
    ) -> SDKResponse[CreditGrantsResponseDTO]:
        """Get credit grants (async).

        Get credit grants (purchases, rollovers, and refunds) for the specified Organization.

        Args:
            organization_id: The id of the Organization.

        Returns:
            (200) CreditGrantsResponseDTO containing credit grants for the current contract.

        Raises:
            ServerError (503): FinOps endpoints are in development with restricted availability. Contact Cribl Support to request access.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(
            f"/v1/organizations/{organization_id}/billing/credits/grants",
            cast_to=CreditGrantsResponseDTO,
        )


class CloudBillingCreditsResource(BaseResource):
    """Credit billing operations (`cloud.billing.credits`)."""

    _surface = "cloud"

    contracts_utilization: CloudBillingCreditsContractsUtilizationResource
    timeseries: CloudBillingCreditsTimeseriesResource
    stats: CloudBillingCreditsStatsResource
    grants: CloudBillingCreditsGrantsResource

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.contracts_utilization = CloudBillingCreditsContractsUtilizationResource(client)
        self.timeseries = CloudBillingCreditsTimeseriesResource(client)
        self.stats = CloudBillingCreditsStatsResource(client)
        self.grants = CloudBillingCreditsGrantsResource(client)


class CloudBillingResource(BaseResource):
    """Billing and FinOps (`cloud.billing`)."""

    _surface = "cloud"

    credits: CloudBillingCreditsResource

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.credits = CloudBillingCreditsResource(client)


class CloudResource(BaseResource):
    """Cribl.Cloud platform API (gateway). Nested groups from openapi/management-plane.yml."""

    _surface = "cloud"

    health: CloudHealthResource
    api_credentials: CloudApiCredentialsResource
    workspaces: CloudWorkspacesResource
    billing: CloudBillingResource

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.health = CloudHealthResource(client)
        self.api_credentials = CloudApiCredentialsResource(client)
        self.workspaces = CloudWorkspacesResource(client)
        self.billing = CloudBillingResource(client)
