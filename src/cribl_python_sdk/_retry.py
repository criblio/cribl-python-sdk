"""Per-operation retry configuration."""
from __future__ import annotations

from dataclasses import dataclass


IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})
NON_IDEMPOTENT_RETRY_ON: tuple[int, ...] = (429,)
IDEMPOTENT_RETRY_ON: tuple[int, ...] = (429, 500, 502, 503, 504)


@dataclass(frozen=True, slots=True)
class RetryConfig:
    """Override retry behavior for individual operations.

    Attrs:
        max_attempts: Maximum number of attempts (including the first). Default: 3.
        backoff_factor: Base for exponential backoff in seconds. Wait = backoff_factor ** attempt. Default: 2.0.
        retry_on: HTTP status codes that trigger a retry for idempotent methods (GET, HEAD, OPTIONS, PUT, DELETE). Default: (429, 500, 502, 503, 504).
        retry_on_non_idempotent: HTTP status codes that trigger a retry for non-idempotent methods (POST, PATCH). Default: (429,).
    """

    max_attempts: int = 3
    """Maximum number of attempts (including the first). Default: 3."""
    backoff_factor: float = 2.0
    """Base for exponential backoff in seconds. Wait = backoff_factor ** attempt. Default: 2.0."""
    retry_on: tuple[int, ...] = IDEMPOTENT_RETRY_ON
    """HTTP status codes that trigger a retry for idempotent methods. Default: (429, 500, 502, 503, 504)."""
    retry_on_non_idempotent: tuple[int, ...] = NON_IDEMPOTENT_RETRY_ON
    """HTTP status codes that trigger a retry for non-idempotent methods (POST, PATCH). Default: (429,)."""

    def retryable_statuses(self, method: str) -> tuple[int, ...]:
        if method.upper() in IDEMPOTENT_METHODS:
            return self.retry_on
        return self.retry_on_non_idempotent
