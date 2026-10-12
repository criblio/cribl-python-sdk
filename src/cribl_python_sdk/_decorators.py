"""SDK method decorators."""
from __future__ import annotations

import warnings
from collections.abc import AsyncIterator, Iterator
from functools import wraps
from typing import Any, Callable, TypeVar

from ._response import SDKResponse

F = TypeVar("F", bound=Callable[..., Any])


def deprecated_endpoint(reason: str) -> Callable[[F], F]:
    """Mark an SDK method as deprecated — emits DeprecationWarning on call."""
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            warnings.warn(
                f"{func.__qualname__} is deprecated: {reason}",
                DeprecationWarning,
                stacklevel=2,
            )
            return func(*args, **kwargs)
        return wrapper  # type: ignore[return-value]
    return decorator


def paginated(method: Callable[..., SDKResponse[Any]], *, page_size: int = 100, **kwargs: Any) -> Iterator[Any]:
    """Auto-paginate a list method that accepts offset/limit kwargs.

    Yields individual items from all pages until exhausted.

    Usage:
        for pipeline in paginated(client.pipelines.list, page_size=50):
            print(pipeline.id)
    """
    return iter_offset_pages(lambda offset, limit: method(offset=offset, limit=limit, **kwargs).data.items, page_size)


def iter_offset_pages(fetch: Callable[[int, int], list[Any]], page_size: int) -> Iterator[Any]:
    """Yield items from ``fetch(offset, limit)`` page by page until a short or empty page."""
    offset = 0
    while True:
        items = fetch(offset, page_size)
        if not items:
            break
        yield from items
        if len(items) < page_size:
            break
        offset += page_size


async def paginated_async(method: Callable[..., Any], *, page_size: int = 100, **kwargs: Any) -> AsyncIterator[Any]:
    """Async auto-pagination — same as paginated() but awaits each page.

    Usage:
        async for pipeline in paginated_async(client.pipelines.list_async, page_size=50):
            print(pipeline.id)
    """
    offset = 0
    while True:
        resp = await method(offset=offset, limit=page_size, **kwargs)
        items = resp.data.items
        if not items:
            break
        for item in items:
            yield item
        if len(items) < page_size:
            break
        offset += page_size
