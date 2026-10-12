"""SDK response wrapper — exposes data, status code, and headers."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

import httpx

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class SDKResponse(Generic[T]):
    """Wrapper around an SDK response providing access to parsed data and raw HTTP metadata.

    Attrs:
        data: The parsed response (typed model).
        status_code: HTTP status code.
        headers: Response headers (case-insensitive mapping).
        raw_response: The full httpx.Response for advanced use.
    """

    data: T
    """The parsed response (typed model)."""
    status_code: int
    """HTTP status code."""
    headers: httpx.Headers
    """Response headers (case-insensitive mapping)."""
    raw_response: httpx.Response
    """The full httpx.Response for advanced use."""
