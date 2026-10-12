"""Database Connections resource."""
from __future__ import annotations

from typing import Any, Literal

from .._response import SDKResponse
from ..models import DatabaseConnectionConfig, PaginatedResponse, TLSClientParams
from ._base import BaseResource


class DatabaseConnectionsResource(BaseResource):
    """Manage Database Connection configurations."""

    def list(
        self,
        *,
        databaseType: Literal["mysql", "oracle", "postgres", "sqlserver", "teradata"] | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> SDKResponse[PaginatedResponse[DatabaseConnectionConfig]]:
        """List all Database Connections.

        Get a list of all Database Connections.

        Args:
            databaseType: Filter results by database engine type. Use this
                parameter to return only Database Connections for the specified
                engine. Valid values: "mysql", "oracle", "postgres", "sqlserver", "teradata".
            limit: Maximum number of Database Connections to return in the
                response for this request. Use with `offset` to paginate the
                response into manageable batches.
            offset: Starting point from which to retrieve results for this
                request. Use with `limit` to paginate the response into
                manageable batches.

        Returns:
            (200) PaginatedResponse containing a list of DatabaseConnectionConfig objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if databaseType is not None:
            params["databaseType"] = databaseType
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._get("/lib/database-connections", cast_to=PaginatedResponse[DatabaseConnectionConfig], params=params or None)

    async def list_async(
        self,
        *,
        databaseType: Literal["mysql", "oracle", "postgres", "sqlserver", "teradata"] | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> SDKResponse[PaginatedResponse[DatabaseConnectionConfig]]:
        """List all Database Connections (async).

        Get a list of all Database Connections.

        Args:
            databaseType: Filter results by database engine type. Use this
                parameter to return only Database Connections for the specified
                engine. Valid values: "mysql", "oracle", "postgres", "sqlserver", "teradata".
            limit: Maximum number of Database Connections to return in the
                response for this request. Use with `offset` to paginate the
                response into manageable batches.
            offset: Starting point from which to retrieve results for this
                request. Use with `limit` to paginate the response into
                manageable batches.

        Returns:
            (200) PaginatedResponse containing a list of DatabaseConnectionConfig objects.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        params: dict[str, Any] = {}
        if databaseType is not None:
            params["databaseType"] = databaseType
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return await self._get_async("/lib/database-connections", cast_to=PaginatedResponse[DatabaseConnectionConfig], params=params or None)

    def create(
        self,
        *,
        id: str,
        databaseType: Literal["mysql", "oracle", "postgres", "sqlserver", "teradata"],
        authType: Literal["configObj", "connectionString", "secret", "secrets"],
        description: str,
        configObj: str | None = None,
        connectionString: str | None = None,
        connectionTimeout: int | None = None,
        credentialsSecret: str | None = None,
        credsSecrets: str | None = None,
        password: str | None = None,
        requestTimeout: int | None = None,
        tags: str | None = None,
        textSecret: str | None = None,
        tls: TLSClientParams | None = None,
        user: str | None = None,
    ) -> SDKResponse[PaginatedResponse[DatabaseConnectionConfig]]:
        """Create a Database Connection.

        Create a new Database Connection.

        Args:
            id: Unique identifier for the Database Connection.
            databaseType: Type of database engine for the connection. Valid values: "mysql", "oracle", "postgres", "sqlserver", "teradata".
            authType: Authentication method for the Database Connection.
                Determines how credentials are provided. Valid values:
                "configObj", "connectionString", "secret", "secrets".
            description: Brief description of the Database Connection.
            configObj: JSON configuration object for advanced SQL Server
                connection settings.
            connectionString: Database connection string with embedded
                credentials or server information.
            connectionTimeout: Maximum time (in milliseconds) to wait when
                establishing the database connection.
            credentialsSecret: Name of the stored credentials secret
                containing username and password for SQL Server configObj
                authentication.
            credsSecrets: Name of the stored credentials secret containing
                username and password. Used with Oracle connections.
            password: Database password for authentication. Used with Oracle
                connections.
            requestTimeout: Maximum time (in milliseconds) to wait for a
                database query to complete. Applies to SQL Server connections
                only.
            tags: Comma-separated list of tags for categorizing and filtering
                Database Connections.
            textSecret: Name of the stored text secret containing the
                connection string.
            tls: TLS client connection settings.
            user: Database username for authentication. Used with Oracle
                connections.

        Returns:
            (200) PaginatedResponse containing the created DatabaseConnectionConfig.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {
            "id": id,
            "databaseType": databaseType,
            "authType": authType,
            "description": description,
        }
        if configObj is not None:
            body["configObj"] = configObj
        if connectionString is not None:
            body["connectionString"] = connectionString
        if connectionTimeout is not None:
            body["connectionTimeout"] = connectionTimeout
        if credentialsSecret is not None:
            body["credentialsSecret"] = credentialsSecret
        if credsSecrets is not None:
            body["credsSecrets"] = credsSecrets
        if password is not None:
            body["password"] = password
        if requestTimeout is not None:
            body["requestTimeout"] = requestTimeout
        if tags is not None:
            body["tags"] = tags
        if textSecret is not None:
            body["textSecret"] = textSecret
        if tls is not None:
            body["tls"] = tls
        if user is not None:
            body["user"] = user
        return self._post("/lib/database-connections", cast_to=PaginatedResponse[DatabaseConnectionConfig], json=body)

    async def create_async(
        self,
        *,
        id: str,
        databaseType: Literal["mysql", "oracle", "postgres", "sqlserver", "teradata"],
        authType: Literal["configObj", "connectionString", "secret", "secrets"],
        description: str,
        configObj: str | None = None,
        connectionString: str | None = None,
        connectionTimeout: int | None = None,
        credentialsSecret: str | None = None,
        credsSecrets: str | None = None,
        password: str | None = None,
        requestTimeout: int | None = None,
        tags: str | None = None,
        textSecret: str | None = None,
        tls: TLSClientParams | None = None,
        user: str | None = None,
    ) -> SDKResponse[PaginatedResponse[DatabaseConnectionConfig]]:
        """Create a Database Connection (async).

        Create a new Database Connection.

        Args:
            id: Unique identifier for the Database Connection.
            databaseType: Type of database engine for the connection. Valid values: "mysql", "oracle", "postgres", "sqlserver", "teradata".
            authType: Authentication method for the Database Connection.
                Determines how credentials are provided. Valid values:
                "configObj", "connectionString", "secret", "secrets".
            description: Brief description of the Database Connection.
            configObj: JSON configuration object for advanced SQL Server
                connection settings.
            connectionString: Database connection string with embedded
                credentials or server information.
            connectionTimeout: Maximum time (in milliseconds) to wait when
                establishing the database connection.
            credentialsSecret: Name of the stored credentials secret
                containing username and password for SQL Server configObj
                authentication.
            credsSecrets: Name of the stored credentials secret containing
                username and password. Used with Oracle connections.
            password: Database password for authentication. Used with Oracle
                connections.
            requestTimeout: Maximum time (in milliseconds) to wait for a
                database query to complete. Applies to SQL Server connections
                only.
            tags: Comma-separated list of tags for categorizing and filtering
                Database Connections.
            textSecret: Name of the stored text secret containing the
                connection string.
            tls: TLS client connection settings.
            user: Database username for authentication. Used with Oracle
                connections.

        Returns:
            (200) PaginatedResponse containing the created DatabaseConnectionConfig.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {
            "id": id,
            "databaseType": databaseType,
            "authType": authType,
            "description": description,
        }
        if configObj is not None:
            body["configObj"] = configObj
        if connectionString is not None:
            body["connectionString"] = connectionString
        if connectionTimeout is not None:
            body["connectionTimeout"] = connectionTimeout
        if credentialsSecret is not None:
            body["credentialsSecret"] = credentialsSecret
        if credsSecrets is not None:
            body["credsSecrets"] = credsSecrets
        if password is not None:
            body["password"] = password
        if requestTimeout is not None:
            body["requestTimeout"] = requestTimeout
        if tags is not None:
            body["tags"] = tags
        if textSecret is not None:
            body["textSecret"] = textSecret
        if tls is not None:
            body["tls"] = tls
        if user is not None:
            body["user"] = user
        return await self._post_async("/lib/database-connections", cast_to=PaginatedResponse[DatabaseConnectionConfig], json=body)

    def get(self, id: str) -> SDKResponse[PaginatedResponse[DatabaseConnectionConfig]]:
        """Get a Database Connection.

        Get the specified Database Connection.

        Args:
            id: The `id` of the Database Connection to get.

        Returns:
            (200) PaginatedResponse containing the requested DatabaseConnectionConfig.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): The requested resource does not exist -- Database Connection not found.
            ServerError (500): Unexpected server error.
        """
        return self._get(f"/lib/database-connections/{id}", cast_to=PaginatedResponse[DatabaseConnectionConfig])

    async def get_async(self, id: str) -> SDKResponse[PaginatedResponse[DatabaseConnectionConfig]]:
        """Get a Database Connection (async).

        Get the specified Database Connection.

        Args:
            id: The `id` of the Database Connection to get.

        Returns:
            (200) PaginatedResponse containing the requested DatabaseConnectionConfig.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): The requested resource does not exist -- Database Connection not found.
            ServerError (500): Unexpected server error.
        """
        return await self._get_async(f"/lib/database-connections/{id}", cast_to=PaginatedResponse[DatabaseConnectionConfig])

    def update(
        self,
        id: str,
        *,
        databaseType: Literal["mysql", "oracle", "postgres", "sqlserver", "teradata"],
        authType: Literal["configObj", "connectionString", "secret", "secrets"],
        description: str,
        configObj: str | None = None,
        connectionString: str | None = None,
        connectionTimeout: int | None = None,
        credentialsSecret: str | None = None,
        credsSecrets: str | None = None,
        password: str | None = None,
        requestTimeout: int | None = None,
        tags: str | None = None,
        textSecret: str | None = None,
        tls: TLSClientParams | None = None,
        user: str | None = None,
    ) -> SDKResponse[PaginatedResponse[DatabaseConnectionConfig]]:
        """Update a Database Connection.

        Update the specified Database Connection.

        Provide a complete representation of the Database Connection that you
        want to update in the request body. This endpoint does not support
        partial updates. Cribl removes any omitted fields when updating the
        Database Connection.

        Confirm that the configuration in your request body is correct before
        sending the request. If the configuration is incorrect, the updated
        Database Connection might not function as expected.

        Args:
            id: The `id` of the Database Connection to update.
            databaseType: Type of database engine for the connection. Valid values: "mysql", "oracle", "postgres", "sqlserver", "teradata".
            authType: Authentication method for the Database Connection.
                Determines how credentials are provided. Valid values:
                "configObj", "connectionString", "secret", "secrets".
            description: Brief description of the Database Connection.
            configObj: JSON configuration object for advanced SQL Server
                connection settings.
            connectionString: Database connection string with embedded
                credentials or server information.
            connectionTimeout: Maximum time (in milliseconds) to wait when
                establishing the database connection.
            credentialsSecret: Name of the stored credentials secret
                containing username and password for SQL Server configObj
                authentication.
            credsSecrets: Name of the stored credentials secret containing
                username and password. Used with Oracle connections.
            password: Database password for authentication. Used with Oracle
                connections.
            requestTimeout: Maximum time (in milliseconds) to wait for a
                database query to complete. Applies to SQL Server connections
                only.
            tags: Comma-separated list of tags for categorizing and filtering
                Database Connections.
            textSecret: Name of the stored text secret containing the
                connection string.
            tls: TLS client connection settings.
            user: Database username for authentication. Used with Oracle
                connections.

        Returns:
            (200) PaginatedResponse containing the updated DatabaseConnectionConfig.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Database Connection not found.
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {
            "databaseType": databaseType,
            "authType": authType,
            "description": description,
        }
        if configObj is not None:
            body["configObj"] = configObj
        if connectionString is not None:
            body["connectionString"] = connectionString
        if connectionTimeout is not None:
            body["connectionTimeout"] = connectionTimeout
        if credentialsSecret is not None:
            body["credentialsSecret"] = credentialsSecret
        if credsSecrets is not None:
            body["credsSecrets"] = credsSecrets
        if password is not None:
            body["password"] = password
        if requestTimeout is not None:
            body["requestTimeout"] = requestTimeout
        if tags is not None:
            body["tags"] = tags
        if textSecret is not None:
            body["textSecret"] = textSecret
        if tls is not None:
            body["tls"] = tls
        if user is not None:
            body["user"] = user
        return self._patch(f"/lib/database-connections/{id}", cast_to=PaginatedResponse[DatabaseConnectionConfig], json=body)

    async def update_async(
        self,
        id: str,
        *,
        databaseType: Literal["mysql", "oracle", "postgres", "sqlserver", "teradata"],
        authType: Literal["configObj", "connectionString", "secret", "secrets"],
        description: str,
        configObj: str | None = None,
        connectionString: str | None = None,
        connectionTimeout: int | None = None,
        credentialsSecret: str | None = None,
        credsSecrets: str | None = None,
        password: str | None = None,
        requestTimeout: int | None = None,
        tags: str | None = None,
        textSecret: str | None = None,
        tls: TLSClientParams | None = None,
        user: str | None = None,
    ) -> SDKResponse[PaginatedResponse[DatabaseConnectionConfig]]:
        """Update a Database Connection (async).

        Update the specified Database Connection.

        Provide a complete representation of the Database Connection that you
        want to update in the request body. This endpoint does not support
        partial updates. Cribl removes any omitted fields when updating the
        Database Connection.

        Confirm that the configuration in your request body is correct before
        sending the request. If the configuration is incorrect, the updated
        Database Connection might not function as expected.

        Args:
            id: The `id` of the Database Connection to update.
            databaseType: Type of database engine for the connection. Valid values: "mysql", "oracle", "postgres", "sqlserver", "teradata".
            authType: Authentication method for the Database Connection.
                Determines how credentials are provided. Valid values:
                "configObj", "connectionString", "secret", "secrets".
            description: Brief description of the Database Connection.
            configObj: JSON configuration object for advanced SQL Server
                connection settings.
            connectionString: Database connection string with embedded
                credentials or server information.
            connectionTimeout: Maximum time (in milliseconds) to wait when
                establishing the database connection.
            credentialsSecret: Name of the stored credentials secret
                containing username and password for SQL Server configObj
                authentication.
            credsSecrets: Name of the stored credentials secret containing
                username and password. Used with Oracle connections.
            password: Database password for authentication. Used with Oracle
                connections.
            requestTimeout: Maximum time (in milliseconds) to wait for a
                database query to complete. Applies to SQL Server connections
                only.
            tags: Comma-separated list of tags for categorizing and filtering
                Database Connections.
            textSecret: Name of the stored text secret containing the
                connection string.
            tls: TLS client connection settings.
            user: Database username for authentication. Used with Oracle
                connections.

        Returns:
            (200) PaginatedResponse containing the updated DatabaseConnectionConfig.

        Raises:
            ValidationError (400): Failed validation or malformed input, such as missing or invalid parameters.
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Database Connection not found.
            ServerError (500): Unexpected server error.
        """
        body: dict[str, Any] = {
            "databaseType": databaseType,
            "authType": authType,
            "description": description,
        }
        if configObj is not None:
            body["configObj"] = configObj
        if connectionString is not None:
            body["connectionString"] = connectionString
        if connectionTimeout is not None:
            body["connectionTimeout"] = connectionTimeout
        if credentialsSecret is not None:
            body["credentialsSecret"] = credentialsSecret
        if credsSecrets is not None:
            body["credsSecrets"] = credsSecrets
        if password is not None:
            body["password"] = password
        if requestTimeout is not None:
            body["requestTimeout"] = requestTimeout
        if tags is not None:
            body["tags"] = tags
        if textSecret is not None:
            body["textSecret"] = textSecret
        if tls is not None:
            body["tls"] = tls
        if user is not None:
            body["user"] = user
        return await self._patch_async(f"/lib/database-connections/{id}", cast_to=PaginatedResponse[DatabaseConnectionConfig], json=body)

    def delete(self, id: str) -> SDKResponse[PaginatedResponse[DatabaseConnectionConfig]]:
        """Delete a Database Connection.

        Delete the specified Database Connection.

        Args:
            id: The `id` of the Database Connection to delete.

        Returns:
            (200) PaginatedResponse containing the deleted DatabaseConnectionConfig.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Database Connection not found.
            ServerError (500): Unexpected server error.
        """
        return self._delete(f"/lib/database-connections/{id}", cast_to=PaginatedResponse[DatabaseConnectionConfig])

    async def delete_async(self, id: str) -> SDKResponse[PaginatedResponse[DatabaseConnectionConfig]]:
        """Delete a Database Connection (async).

        Delete the specified Database Connection.

        Args:
            id: The `id` of the Database Connection to delete.

        Returns:
            (200) PaginatedResponse containing the deleted DatabaseConnectionConfig.

        Raises:
            AuthenticationError (401): Authentication failed (missing or invalid credentials or Bearer token).
            NotFoundError (404): Database Connection not found.
            ServerError (500): Unexpected server error.
        """
        return await self._delete_async(f"/lib/database-connections/{id}", cast_to=PaginatedResponse[DatabaseConnectionConfig])
