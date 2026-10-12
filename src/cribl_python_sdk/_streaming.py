"""NDJSON streaming helpers for Cribl API endpoints that return line-delimited JSON."""
from __future__ import annotations

import json
from collections.abc import Generator, AsyncGenerator
from typing import TypeVar

import httpx

from .models import CriblModel

T = TypeVar("T", bound=CriblModel)


def iter_ndjson(response: httpx.Response, model: type[T]) -> Generator[T, None, None]:
    """Yield parsed model instances from an NDJSON response, line by line.

    Each line is parsed as JSON and validated through the given Pydantic model.
    Blank lines are skipped.
    """
    for line in response.iter_lines():
        line = line.strip()
        if not line:
            continue
        data = json.loads(line)
        yield model.model_validate(data)


async def aiter_ndjson(response: httpx.Response, model: type[T]) -> AsyncGenerator[T, None]:
    """Yield parsed model instances from an async NDJSON response, line by line."""
    async for line in response.aiter_lines():
        line = line.strip()
        if not line:
            continue
        data = json.loads(line)
        yield model.model_validate(data)
