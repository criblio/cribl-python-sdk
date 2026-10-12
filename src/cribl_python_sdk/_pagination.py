"""Auto-pagination helper for offset/limit endpoints."""
from __future__ import annotations

from typing import Any, Callable, Iterator

from ._decorators import iter_offset_pages


def paginate(method: Callable[..., list[dict[str, Any]]], **kwargs: Any) -> Iterator[dict[str, Any]]:
    """Auto-paginate an offset/limit list method.

    Yields all items across pages until exhausted.
    """
    limit = kwargs.pop("limit", 100)
    return iter_offset_pages(lambda offset, limit: method(offset=offset, limit=limit, **kwargs), limit)
