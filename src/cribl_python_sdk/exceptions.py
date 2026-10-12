"""Typed exception hierarchy for the Cribl SDK."""
from __future__ import annotations

import httpx


class APIError(Exception):
    """Base API error with status code and response context."""

    def __init__(self, status_code: int, message: str, response: httpx.Response | None = None):
        self.status_code = status_code
        self.message = message
        self.response = response
        super().__init__(f"HTTP {status_code}: {message}")

    @classmethod
    def from_response(cls, resp: httpx.Response) -> APIError:
        """Create the appropriate error subclass from an HTTP response."""
        try:
            body = resp.json()
            msg = body.get("message") or body.get("error") or resp.text
        except Exception:
            msg = resp.text
        error_map: dict[int, type[APIError]] = {
            401: AuthenticationError,
            403: AuthorizationError,
            404: NotFoundError,
            422: ValidationError,
            429: RateLimitError,
        }
        klass = error_map.get(resp.status_code, ServerError if resp.status_code >= 500 else cls)
        return klass(resp.status_code, msg, resp)


class AuthenticationError(APIError):
    """401 — missing or invalid credentials."""


class AuthorizationError(APIError):
    """403 — insufficient permissions."""


class NotFoundError(APIError):
    """404 — resource not found."""


class ValidationError(APIError):
    """422 — request validation failed."""


class RateLimitError(APIError):
    """429 — rate limit exceeded."""


class ServerError(APIError):
    """5xx — unexpected server error."""


class ConnectionError(Exception):
    """Cannot reach the Cribl server."""

    def __init__(self, url: str, original: Exception):
        self.url = url
        self.original = original
        super().__init__(f"Cannot connect to {url}: {original}")


class TimeoutError(Exception):
    """Request timed out."""

    def __init__(self, method: str, path: str, timeout: float, original: Exception):
        self.method = method
        self.path = path
        self.timeout = timeout
        self.original = original
        super().__init__(f"{method} {path} timed out after {timeout}s")


class ResponseValidationError(Exception):
    """Response body could not be parsed into the expected model."""

    def __init__(self, url: str, status_code: int, body: str, original: Exception):
        self.url = url
        self.status_code = status_code
        self.body = body
        self.original = original
        super().__init__(f"Failed to parse response from {url} (HTTP {status_code}): {original}")
