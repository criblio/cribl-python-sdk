"""Authentication resource."""
from __future__ import annotations

from typing import TYPE_CHECKING

from .._response import SDKResponse
from ..models import AuthToken
from ._base import BaseResource

if TYPE_CHECKING:
    from ..client import Cribl


class AuthTokensResource(BaseResource):
    """Authentication token operations (`auth.tokens`)."""

    def get(self, *, username: str, password: str) -> SDKResponse[AuthToken]:
        """Log in and fetch an authentication token.

        This endpoint is unavailable on Cribl.Cloud. Instead, follow the
        instructions at https://docs.cribl.io/stream/api-tutorials/#criblcloud
        to get an Auth token for Cribl.Cloud.

        Args:
            username: Username of the account to authenticate.
            password: Password for the account.

        Returns:
            (200) AuthToken containing the authentication token.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return self._post("/auth/login", cast_to=AuthToken, json={"username": username, "password": password})

    async def get_async(self, *, username: str, password: str) -> SDKResponse[AuthToken]:
        """Log in and fetch an authentication token (async).

        This endpoint is unavailable on Cribl.Cloud. Instead, follow the
        instructions at https://docs.cribl.io/stream/api-tutorials/#criblcloud
        to get an Auth token for Cribl.Cloud.

        Args:
            username: Username of the account to authenticate.
            password: Password for the account.

        Returns:
            (200) AuthToken containing the authentication token.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        return await self._post_async("/auth/login", cast_to=AuthToken, json={"username": username, "password": password})


class AuthResource(BaseResource):
    """Authentication operations (login for on-prem deployments)."""

    def __init__(self, client: Cribl):
        super().__init__(client)
        self.tokens = AuthTokensResource(client)
