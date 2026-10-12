"""Versioning (Git) resource."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List

from .._response import SDKResponse
from ..models import (
    BranchInfo,
    CurrentBranchResult,
    GitCommitSummary,
    GitCountResult,
    GitDiffResult,
    GitFilesResponse,
    GitInfo,
    GitLogResult,
    GitRevertResult,
    GitShowResult,
    GitStatusResult,
    PaginatedResponse,
)
from ._base import BaseResource

if TYPE_CHECKING:
    from ..client import Cribl



class VersioningBranchesResource(BaseResource):
    """Branch operations (`versioning.branches`)."""

    # GET /version/branch

    def list(self) -> SDKResponse[PaginatedResponse[BranchInfo]]:
        """List all branches in the Git repository used for Cribl configuration.

        Get a list of all branches in the Git repository used for Cribl
        configuration.

        Returns:
            (200) PaginatedResponse containing the requested BranchInfo.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get("/version/branch", cast_to=PaginatedResponse[BranchInfo])

    async def list_async(self) -> SDKResponse[PaginatedResponse[BranchInfo]]:
        """List all branches in the Git repository used for Cribl configuration (async).

        Get a list of all branches in the Git repository used for Cribl
        configuration.

        Returns:
            (200) PaginatedResponse containing the requested BranchInfo.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async("/version/branch", cast_to=PaginatedResponse[BranchInfo])

    # GET /version/current-branch

    def get(self) -> SDKResponse[CurrentBranchResult]:
        """Get the name of the Git branch that the Cribl configuration is checked out to.

        Useful for verifying the active configuration branch.

        Returns:
            (200) CurrentBranchResult with the active branch name.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get("/version/current-branch", cast_to=CurrentBranchResult)

    async def get_async(self) -> SDKResponse[CurrentBranchResult]:
        """Get the name of the Git branch that the Cribl configuration is checked out to (async).

        Useful for verifying the active configuration branch.

        Returns:
            (200) CurrentBranchResult with the active branch name.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async("/version/current-branch", cast_to=CurrentBranchResult)


class VersioningCommitsFilesResource(BaseResource):
    """Commit file operations (`versioning.commits.files`)."""

    # GET /version/count

    def count(self, *, commit: str | None = None) -> SDKResponse[PaginatedResponse[GitCountResult]]:
        """Get a count of files that changed since a commit.

        Get a count of the files that changed since a commit. Default is the
        latest commit (HEAD).

        Args:
            commit: The Git commit hash to use as the starting point for the count.

        Returns:
            (200) PaginatedResponse containing the requested GitCountResult.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if commit is not None:
            params["commit"] = commit
        return self._get("/version/count", cast_to=PaginatedResponse[GitCountResult], params=params)

    async def count_async(self, *, commit: str | None = None) -> SDKResponse[PaginatedResponse[GitCountResult]]:
        """Get a count of files that changed since a commit (async).

        Get a count of the files that changed since a commit. Default is the
        latest commit (HEAD).

        Args:
            commit: The Git commit hash to use as the starting point for the count.

        Returns:
            (200) PaginatedResponse containing the requested GitCountResult.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if commit is not None:
            params["commit"] = commit
        return await self._get_async("/version/count", cast_to=PaginatedResponse[GitCountResult], params=params)

    # GET /version/files

    def list(self, *, commit: str | None = None) -> SDKResponse[PaginatedResponse[GitFilesResponse]]:
        """Get the names and statuses of files that changed since a commit.

        Default is the latest commit (HEAD).

        Args:
            commit: The Git commit hash to use as the starting point for the request.

        Returns:
            (200) PaginatedResponse containing the requested GitFilesResponse.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if commit is not None:
            params["commit"] = commit
        return self._get("/version/files", cast_to=PaginatedResponse[GitFilesResponse], params=params)

    async def list_async(self, *, commit: str | None = None) -> SDKResponse[PaginatedResponse[GitFilesResponse]]:
        """Get the names and statuses of files that changed since a commit (async).

        Default is the latest commit (HEAD).

        Args:
            commit: The Git commit hash to use as the starting point for the request.

        Returns:
            (200) PaginatedResponse containing the requested GitFilesResponse.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if commit is not None:
            params["commit"] = commit
        return await self._get_async("/version/files", cast_to=PaginatedResponse[GitFilesResponse], params=params)


class VersioningCommitsResource(BaseResource):
    """Commit operations (`versioning.commits`)."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.files = VersioningCommitsFilesResource(client)

    # GET /version

    def list(
        self,
        *,
        count: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[GitLogResult]]:
        """List the commit history.

        Analogous to `git log` for the Cribl configuration, allowing you to
        audit and review changes over time.

        Args:
            count: Maximum number of commits to read from the commit history. When provided, `offset` and `limit` are applied to that read set.
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing GitLogResult objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if count is not None:
            params["count"] = count
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get("/version", cast_to=PaginatedResponse[GitLogResult], params=params)

    async def list_async(
        self,
        *,
        count: int | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[GitLogResult]]:
        """List the commit history (async).

        Analogous to `git log` for the Cribl configuration, allowing you to
        audit and review changes over time.

        Args:
            count: Maximum number of commits to read from the commit history. When provided, `offset` and `limit` are applied to that read set.
            offset: Pagination offset.
            limit: Maximum number of items to return.

        Returns:
            (200) PaginatedResponse containing GitLogResult objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if count is not None:
            params["count"] = count
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return await self._get_async("/version", cast_to=PaginatedResponse[GitLogResult], params=params)

    # POST /version/commit

    def create(
        self,
        *,
        message: str,
        effective: bool | None = None,
        files: List[str] | None = None,
    ) -> SDKResponse[PaginatedResponse[GitCommitSummary]]:
        """Create a new commit for pending changes to the Cribl configuration.

        Any merge conflicts indicated in the response must be resolved using
        Git.

        To commit only a subset of configuration changes, specify the files to
        include in the commit in the `files` array.

        Args:
            message: Commit message to use for the new Git commit.
            effective: If `true`, apply the commit to the group's effective configuration. Requires a group context.
            files: Array of file paths to include in the commit, relative to the configuration root. If omitted, all pending changes are committed.

        Returns:
            (200) PaginatedResponse containing GitCommitSummary objects.

        Raises:
            ValidationError (400): When effective: true is provided without a group context.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"message": message}
        if effective is not None:
            body["effective"] = effective
        if files is not None:
            body["files"] = files
        return self._post("/version/commit", cast_to=PaginatedResponse[GitCommitSummary], json=body)

    async def create_async(
        self,
        *,
        message: str,
        effective: bool | None = None,
        files: List[str] | None = None,
    ) -> SDKResponse[PaginatedResponse[GitCommitSummary]]:
        """Create a new commit for pending changes to the Cribl configuration (async).

        Any merge conflicts indicated in the response must be resolved using
        Git.

        To commit only a subset of configuration changes, specify the files to
        include in the commit in the `files` array.

        Args:
            message: Commit message to use for the new Git commit.
            effective: If `true`, apply the commit to the group's effective configuration. Requires a group context.
            files: Array of file paths to include in the commit, relative to the configuration root. If omitted, all pending changes are committed.

        Returns:
            (200) PaginatedResponse containing GitCommitSummary objects.

        Raises:
            ValidationError (400): When effective: true is provided without a group context.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"message": message}
        if effective is not None:
            body["effective"] = effective
        if files is not None:
            body["files"] = files
        return await self._post_async("/version/commit", cast_to=PaginatedResponse[GitCommitSummary], json=body)

    # GET /version/diff

    def diff(
        self,
        *,
        commit: str | None = None,
        filename: str | None = None,
        diffLineLimit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[GitDiffResult]]:
        """Get the diff for a commit.

        Default is the latest commit (HEAD).

        Args:
            commit: The Git commit hash to get the diff for.
            filename: The relative path of the file to get the diff for.
            diffLineLimit: Number of lines of the diff to return. Default is 1000. Set to 0 to return the full diff, regardless of the number of lines.

        Returns:
            (200) PaginatedResponse containing the requested GitDiffResult.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if commit is not None:
            params["commit"] = commit
        if filename is not None:
            params["filename"] = filename
        if diffLineLimit is not None:
            params["diffLineLimit"] = diffLineLimit
        return self._get("/version/diff", cast_to=PaginatedResponse[GitDiffResult], params=params)

    async def diff_async(
        self,
        *,
        commit: str | None = None,
        filename: str | None = None,
        diffLineLimit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[GitDiffResult]]:
        """Get the diff for a commit (async).

        Default is the latest commit (HEAD).

        Args:
            commit: The Git commit hash to get the diff for.
            filename: The relative path of the file to get the diff for.
            diffLineLimit: Number of lines of the diff to return. Default is 1000. Set to 0 to return the full diff, regardless of the number of lines.

        Returns:
            (200) PaginatedResponse containing the requested GitDiffResult.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if commit is not None:
            params["commit"] = commit
        if filename is not None:
            params["filename"] = filename
        if diffLineLimit is not None:
            params["diffLineLimit"] = diffLineLimit
        return await self._get_async("/version/diff", cast_to=PaginatedResponse[GitDiffResult], params=params)

    # POST /version/push

    def push(self) -> SDKResponse[PaginatedResponse[str]]:
        """Push local commits to the remote repository.

        Push all local commits from the local repository to the remote
        repository.

        Requires at least one local commit that has not been pushed. Returns an
        error if the remote repository cannot be reached or the push is
        rejected.

        Returns:
            (200) PaginatedResponse containing str objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._post("/version/push", cast_to=PaginatedResponse[str], json={})

    async def push_async(self) -> SDKResponse[PaginatedResponse[str]]:
        """Push local commits to the remote repository (async).

        Push all local commits from the local repository to the remote
        repository.

        Requires at least one local commit that has not been pushed. Returns an
        error if the remote repository cannot be reached or the push is
        rejected.

        Returns:
            (200) PaginatedResponse containing str objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._post_async("/version/push", cast_to=PaginatedResponse[str], json={})

    # POST /version/revert

    def revert(
        self,
        *,
        commit: str,
        force: bool | None = None,
        message: str | None = None,
    ) -> SDKResponse[PaginatedResponse[GitRevertResult]]:
        """Revert a commit in the local repository.

        Revert a commit in the local repository by creating a new commit that
        undoes the changes introduced by the specified commit.

        Use the `force` field to proceed even when the working directory is not
        clean.

        Args:
            commit: SHA-1 hash of the commit to revert.
            force: If `true`, force the revert even when the working directory is not clean. Otherwise, `false`.
            message: Custom message to use for the revert commit. If omitted, a default message is generated.

        Returns:
            (200) PaginatedResponse containing GitRevertResult objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"commit": commit}
        if force is not None:
            body["force"] = force
        if message is not None:
            body["message"] = message
        return self._post("/version/revert", cast_to=PaginatedResponse[GitRevertResult], json=body)

    async def revert_async(
        self,
        *,
        commit: str,
        force: bool | None = None,
        message: str | None = None,
    ) -> SDKResponse[PaginatedResponse[GitRevertResult]]:
        """Revert a commit in the local repository (async).

        Revert a commit in the local repository by creating a new commit that
        undoes the changes introduced by the specified commit.

        Use the `force` field to proceed even when the working directory is not
        clean.

        Args:
            commit: SHA-1 hash of the commit to revert.
            force: If `true`, force the revert even when the working directory is not clean. Otherwise, `false`.
            message: Custom message to use for the revert commit. If omitted, a default message is generated.

        Returns:
            (200) PaginatedResponse containing GitRevertResult objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {"commit": commit}
        if force is not None:
            body["force"] = force
        if message is not None:
            body["message"] = message
        return await self._post_async("/version/revert", cast_to=PaginatedResponse[GitRevertResult], json=body)

    # GET /version/show

    def get(
        self,
        *,
        commit: str | None = None,
        filename: str | None = None,
        diffLineLimit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[GitShowResult]]:
        """Get the diff and log message for a commit.

        Default is the latest commit (HEAD).

        Args:
            commit: The Git commit hash to retrieve the diff and log message for.
            filename: The relative path of the file to get the diff and log message for.
            diffLineLimit: Number of lines of the diff to return. Default is 1000. Set to 0 to return the full diff, regardless of the number of lines.

        Returns:
            (200) PaginatedResponse containing the requested GitShowResult.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if commit is not None:
            params["commit"] = commit
        if filename is not None:
            params["filename"] = filename
        if diffLineLimit is not None:
            params["diffLineLimit"] = diffLineLimit
        return self._get("/version/show", cast_to=PaginatedResponse[GitShowResult], params=params)

    async def get_async(
        self,
        *,
        commit: str | None = None,
        filename: str | None = None,
        diffLineLimit: int | None = None,
    ) -> SDKResponse[PaginatedResponse[GitShowResult]]:
        """Get the diff and log message for a commit (async).

        Default is the latest commit (HEAD).

        Args:
            commit: The Git commit hash to retrieve the diff and log message for.
            filename: The relative path of the file to get the diff and log message for.
            diffLineLimit: Number of lines of the diff to return. Default is 1000. Set to 0 to return the full diff, regardless of the number of lines.

        Returns:
            (200) PaginatedResponse containing the requested GitShowResult.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if commit is not None:
            params["commit"] = commit
        if filename is not None:
            params["filename"] = filename
        if diffLineLimit is not None:
            params["diffLineLimit"] = diffLineLimit
        return await self._get_async("/version/show", cast_to=PaginatedResponse[GitShowResult], params=params)

    # POST /version/undo

    def undo(self) -> SDKResponse[PaginatedResponse[bool]]:
        """Discard uncommitted (staged) changes.

        Discard all uncommitted (staged) configuration changes, resetting the
        working directory to the last committed state. Use only if you are
        certain that you do not need to preserve your local changes.

        When applied globally (no group), triggers a Cribl restart to reload the
        reverted configuration. Returns `false` if the working directory is
        already clean.

        Returns:
            (200) PaginatedResponse containing bool objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._post("/version/undo", cast_to=PaginatedResponse[bool], json={})

    async def undo_async(self) -> SDKResponse[PaginatedResponse[bool]]:
        """Discard uncommitted (staged) changes (async).

        Discard all uncommitted (staged) configuration changes, resetting the
        working directory to the last committed state. Use only if you are
        certain that you do not need to preserve your local changes.

        When applied globally (no group), triggers a Cribl restart to reload the
        reverted configuration. Returns `false` if the working directory is
        already clean.

        Returns:
            (200) PaginatedResponse containing bool objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._post_async("/version/undo", cast_to=PaginatedResponse[bool], json={})


class VersioningConfigsResource(BaseResource):
    """Config operations (`versioning.configs`)."""

    # GET /version/info

    def get(self) -> SDKResponse[PaginatedResponse[GitInfo]]:
        """Get the configuration and status for the Git integration.

        Get the configuration and versioning status for the Git integration for
        the Cribl configuration.

        Returns:
            (200) PaginatedResponse containing the requested GitInfo.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get("/version/info", cast_to=PaginatedResponse[GitInfo])

    async def get_async(self) -> SDKResponse[PaginatedResponse[GitInfo]]:
        """Get the configuration and status for the Git integration (async).

        Get the configuration and versioning status for the Git integration for
        the Cribl configuration.

        Returns:
            (200) PaginatedResponse containing the requested GitInfo.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async("/version/info", cast_to=PaginatedResponse[GitInfo])


class VersioningStatusesResource(BaseResource):
    """Status operations (`versioning.statuses`)."""

    # GET /version/status

    def get(self) -> SDKResponse[PaginatedResponse[GitStatusResult]]:
        """Get the status of the current working tree.

        Get the status of the current working tree of the Git repository used
        for Cribl configuration. The response includes details about modified,
        staged, untracked, and conflicted files, as well as branch and remote
        tracking information.

        Returns:
            (200) PaginatedResponse containing the requested GitStatusResult.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._get("/version/status", cast_to=PaginatedResponse[GitStatusResult])

    async def get_async(self) -> SDKResponse[PaginatedResponse[GitStatusResult]]:
        """Get the status of the current working tree (async).

        Get the status of the current working tree of the Git repository used
        for Cribl configuration. The response includes details about modified,
        staged, untracked, and conflicted files, as well as branch and remote
        tracking information.

        Returns:
            (200) PaginatedResponse containing the requested GitStatusResult.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._get_async("/version/status", cast_to=PaginatedResponse[GitStatusResult])


class VersioningResource(BaseResource):
    """Manage Git versioning for Cribl configuration."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.branches = VersioningBranchesResource(client)
        self.commits = VersioningCommitsResource(client)
        self.configs = VersioningConfigsResource(client)
        self.statuses = VersioningStatusesResource(client)
