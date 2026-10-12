"""Packs resource."""
from __future__ import annotations

from typing import Any

from .._response import SDKResponse
from ..models import PackInfo, PackInstallInfo, PackTagsParam, PackUninstallInfo, PaginatedResponse, UploadPackResponse
from ._base import BaseResource


class PacksResource(BaseResource):
    """Manage Packs — bundled, reusable configurations."""

    def list(
        self,
        *,
        with_: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[PackInfo]]:
        """List all Packs.

        Get a list of all Packs.

        Args:
            with_: Comma-separated list of additional properties to include in
                the response. When set, the response includes a count of each
                specified property in each Pack. Supported values: `inputs`,
                `outputs`, `collectors`.
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing a list of PackInfo objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if with_ is not None:
            params["with"] = with_
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get("/packs", cast_to=PaginatedResponse[PackInfo], params=params or None)

    async def list_async(
        self,
        *,
        with_: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[PackInfo]]:
        """List all Packs (async).

        Get a list of all Packs.

        Args:
            with_: Comma-separated list of additional properties to include in
                the response. When set, the response includes a count of each
                specified property in each Pack. Supported values: `inputs`,
                `outputs`, `collectors`.
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing a list of PackInfo objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if with_ is not None:
            params["with"] = with_
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return await self._get_async("/packs", cast_to=PaginatedResponse[PackInfo], params=params or None)

    def install(
        self,
        *,
        id: str | None = None,
        spec: str | None = None,
        version: str | None = None,
        minLogStreamVersion: str | None = None,
        displayName: str | None = None,
        author: str | None = None,
        description: str | None = None,
        source: str | None = None,
        tags: PackTagsParam | None = None,
        allowCustomFunctions: bool | None = None,
        force: bool | None = None,
    ) -> SDKResponse[PaginatedResponse[PackInstallInfo]]:
        """Install a Pack.

        Install a Pack.

        To install an uploaded Pack, provide the `source` value from the
        `PUT /packs` response as the `source` parameter in the request body.

        To install a Pack by importing from a URL, provide the direct URL
        location of the `.crbl` file for the Pack as the `source` parameter in
        the request body.

        To install a Pack by importing from a Git repository, provide
        `git+<repo-url>` as the `source` parameter in the request body.

        If you do not include the `source` parameter in the request body, an
        empty Pack is created.

        Args:
            id: Unique identifier for the Pack.
            spec: Semver range constraint to apply when resolving the Pack
                version to install.
            version: Version of the Pack, following semantic versioning.
            minLogStreamVersion: Minimum version of Cribl Stream required to
                run this Pack.
            displayName: Human-readable display name for the Pack.
            author: Name or identifier of the Pack author.
            description: Brief description of the Pack and its purpose.
            source: Source of the Pack. Provide a staging source ID from
                `PUT /packs`, a direct URL to a `.crbl` file, or a
                `git+<repo-url>` Git repository URL. If omitted, an empty
                Pack is created.
            tags: Categorization tags for the Pack.
            allowCustomFunctions: If `true` or omitted, allow the Pack to use
                custom JavaScript functions. If `false`, reject Packs that
                use custom JavaScript functions.
            force: If `true`, overwrite an existing Pack with the same ID.
                Otherwise, `false`.

        Returns:
            (200) PaginatedResponse containing PackInstallInfo objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {}
        if id is not None:
            body["id"] = id
        if spec is not None:
            body["spec"] = spec
        if version is not None:
            body["version"] = version
        if minLogStreamVersion is not None:
            body["minLogStreamVersion"] = minLogStreamVersion
        if displayName is not None:
            body["displayName"] = displayName
        if author is not None:
            body["author"] = author
        if description is not None:
            body["description"] = description
        if source is not None:
            body["source"] = source
        if tags is not None:
            body["tags"] = tags
        if allowCustomFunctions is not None:
            body["allowCustomFunctions"] = allowCustomFunctions
        if force is not None:
            body["force"] = force
        return self._post("/packs", cast_to=PaginatedResponse[PackInstallInfo], json=body)

    async def install_async(
        self,
        *,
        id: str | None = None,
        spec: str | None = None,
        version: str | None = None,
        minLogStreamVersion: str | None = None,
        displayName: str | None = None,
        author: str | None = None,
        description: str | None = None,
        source: str | None = None,
        tags: PackTagsParam | None = None,
        allowCustomFunctions: bool | None = None,
        force: bool | None = None,
    ) -> SDKResponse[PaginatedResponse[PackInstallInfo]]:
        """Install a Pack (async).

        Install a Pack.

        To install an uploaded Pack, provide the `source` value from the
        `PUT /packs` response as the `source` parameter in the request body.

        To install a Pack by importing from a URL, provide the direct URL
        location of the `.crbl` file for the Pack as the `source` parameter in
        the request body.

        To install a Pack by importing from a Git repository, provide
        `git+<repo-url>` as the `source` parameter in the request body.

        If you do not include the `source` parameter in the request body, an
        empty Pack is created.

        Args:
            id: Unique identifier for the Pack.
            spec: Semver range constraint to apply when resolving the Pack
                version to install.
            version: Version of the Pack, following semantic versioning.
            minLogStreamVersion: Minimum version of Cribl Stream required to
                run this Pack.
            displayName: Human-readable display name for the Pack.
            author: Name or identifier of the Pack author.
            description: Brief description of the Pack and its purpose.
            source: Source of the Pack. Provide a staging source ID from
                `PUT /packs`, a direct URL to a `.crbl` file, or a
                `git+<repo-url>` Git repository URL. If omitted, an empty
                Pack is created.
            tags: Categorization tags for the Pack.
            allowCustomFunctions: If `true` or omitted, allow the Pack to use
                custom JavaScript functions. If `false`, reject Packs that
                use custom JavaScript functions.
            force: If `true`, overwrite an existing Pack with the same ID.
                Otherwise, `false`.

        Returns:
            (200) PaginatedResponse containing PackInstallInfo objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {}
        if id is not None:
            body["id"] = id
        if spec is not None:
            body["spec"] = spec
        if version is not None:
            body["version"] = version
        if minLogStreamVersion is not None:
            body["minLogStreamVersion"] = minLogStreamVersion
        if displayName is not None:
            body["displayName"] = displayName
        if author is not None:
            body["author"] = author
        if description is not None:
            body["description"] = description
        if source is not None:
            body["source"] = source
        if tags is not None:
            body["tags"] = tags
        if allowCustomFunctions is not None:
            body["allowCustomFunctions"] = allowCustomFunctions
        if force is not None:
            body["force"] = force
        return await self._post_async("/packs", cast_to=PaginatedResponse[PackInstallInfo], json=body)

    def upload(self, *, filename: str, content: bytes) -> SDKResponse[UploadPackResponse]:
        """Upload a Pack file.

        Upload a Pack file. Returns the `source` ID needed to install the Pack
        with `POST /packs`, which you must call separately.

        Args:
            filename: Filename of the Pack file to upload.
            content: Binary content of the Pack file.

        Returns:
            (200) UploadPackResponse with the source ID for installation.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._put("/packs", cast_to=UploadPackResponse, params={"filename": filename}, content=content)

    async def upload_async(self, *, filename: str, content: bytes) -> SDKResponse[UploadPackResponse]:
        """Upload a Pack file (async).

        Upload a Pack file. Returns the `source` ID needed to install the Pack
        with `POST /packs`, which you must call separately.

        Args:
            filename: Filename of the Pack file to upload.
            content: Binary content of the Pack file.

        Returns:
            (200) UploadPackResponse with the source ID for installation.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._put_async("/packs", cast_to=UploadPackResponse, params={"filename": filename}, content=content)

    def get(self, id: str) -> SDKResponse[PaginatedResponse[PackInfo]]:
        """Get a Pack.

        Get the specified Pack.

        Args:
            id: The `id` of the Pack to get. Use the `id` field from the list
                response.

        Returns:
            (200) PaginatedResponse containing the requested PackInfo.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get(f"/packs/{id}", cast_to=PaginatedResponse[PackInfo])

    async def get_async(self, id: str) -> SDKResponse[PaginatedResponse[PackInfo]]:
        """Get a Pack (async).

        Get the specified Pack.

        Args:
            id: The `id` of the Pack to get. Use the `id` field from the list
                response.

        Returns:
            (200) PaginatedResponse containing the requested PackInfo.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"/packs/{id}", cast_to=PaginatedResponse[PackInfo])

    def upgrade(
        self,
        id: str,
        *,
        source: str,
        spec: str | None = None,
        minor: bool | None = None,
        allowCustomFunctions: bool | None = None,
    ) -> SDKResponse[PaginatedResponse[PackInfo]]:
        """Upgrade a Pack.

        Upgrade the specified Pack.

        If the Pack includes any user-modified versions of default Cribl
        Knowledge resources such as lookups, copy the modified files locally for
        safekeeping before upgrading the Pack. Copy the modified files back to
        the upgraded Pack after you install it with `POST /packs` to overwrite
        the default versions in the Pack.

        After you upgrade the Pack, update any Routes, Pipelines, Sources, and
        Destinations that use the previous Pack version so that they reference
        the upgraded Pack.

        Args:
            id: The `id` of the Pack to upgrade. Use the `id` field from the
                list response.
            source: Source of the upgraded Pack. Use the `source` value returned
                by `PUT /packs` for an uploaded file, or provide a direct URL to
                a `.crbl` file or a `git+<repo-url>` Git repository URL.
            spec: Semver range constraint to apply when resolving the Pack
                version to install.
            minor: If `true`, allow the upgrade to install a minor (non-breaking)
                version. Otherwise, `false`.
            allowCustomFunctions: If `true` or omitted, allow the Pack to use
                custom JavaScript functions. If `false`, reject Packs that use
                custom JavaScript functions.

        Returns:
            (200) PaginatedResponse containing PackInfo objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"source": source}
        if spec is not None:
            body["spec"] = spec
        if minor is not None:
            body["minor"] = minor
        if allowCustomFunctions is not None:
            body["allowCustomFunctions"] = allowCustomFunctions
        return self._patch(f"/packs/{id}", cast_to=PaginatedResponse[PackInfo], json=body)

    async def upgrade_async(
        self,
        id: str,
        *,
        source: str,
        spec: str | None = None,
        minor: bool | None = None,
        allowCustomFunctions: bool | None = None,
    ) -> SDKResponse[PaginatedResponse[PackInfo]]:
        """Upgrade a Pack (async).

        Upgrade the specified Pack.

        If the Pack includes any user-modified versions of default Cribl
        Knowledge resources such as lookups, copy the modified files locally for
        safekeeping before upgrading the Pack. Copy the modified files back to
        the upgraded Pack after you install it with `POST /packs` to overwrite
        the default versions in the Pack.

        After you upgrade the Pack, update any Routes, Pipelines, Sources, and
        Destinations that use the previous Pack version so that they reference
        the upgraded Pack.

        Args:
            id: The `id` of the Pack to upgrade. Use the `id` field from the
                list response.
            source: Source of the upgraded Pack. Use the `source` value returned
                by `PUT /packs` for an uploaded file, or provide a direct URL to
                a `.crbl` file or a `git+<repo-url>` Git repository URL.
            spec: Semver range constraint to apply when resolving the Pack
                version to install.
            minor: If `true`, allow the upgrade to install a minor (non-breaking)
                version. Otherwise, `false`.
            allowCustomFunctions: If `true` or omitted, allow the Pack to use
                custom JavaScript functions. If `false`, reject Packs that use
                custom JavaScript functions.

        Returns:
            (200) PaginatedResponse containing PackInfo objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"source": source}
        if spec is not None:
            body["spec"] = spec
        if minor is not None:
            body["minor"] = minor
        if allowCustomFunctions is not None:
            body["allowCustomFunctions"] = allowCustomFunctions
        return await self._patch_async(f"/packs/{id}", cast_to=PaginatedResponse[PackInfo], json=body)

    def uninstall(self, id: str) -> SDKResponse[PaginatedResponse[PackUninstallInfo]]:
        """Uninstall a Pack.

        Uninstall the specified Pack.

        Args:
            id: The `id` of the Pack to uninstall. Use the `id` field from the
                list response.

        Returns:
            (200) PaginatedResponse containing PackUninstallInfo objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._delete(f"/packs/{id}", cast_to=PaginatedResponse[PackUninstallInfo])

    async def uninstall_async(self, id: str) -> SDKResponse[PaginatedResponse[PackUninstallInfo]]:
        """Uninstall a Pack (async).

        Uninstall the specified Pack.

        Args:
            id: The `id` of the Pack to uninstall. Use the `id` field from the
                list response.

        Returns:
            (200) PaginatedResponse containing PackUninstallInfo objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._delete_async(f"/packs/{id}", cast_to=PaginatedResponse[PackUninstallInfo])
