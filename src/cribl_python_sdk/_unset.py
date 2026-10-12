"""UNSET sentinel for distinguishing 'not provided' from None in PATCH methods."""
from __future__ import annotations

from enum import Enum
from typing import TypeVar, Union

T = TypeVar("T")


class _UnsetType(Enum):
    """Sentinel enum — single member, used as default for optional PATCH fields."""
    UNSET = "UNSET"

    def __repr__(self) -> str:
        return "UNSET"

    def __bool__(self) -> bool:
        return False


UNSET: _UnsetType = _UnsetType.UNSET
"""Sentinel value indicating a field was not provided (distinct from None which means 'set to null')."""

Nullable = Union[T, None, _UnsetType]
"""Type alias for PATCH fields: T | None | UNSET. Use as default=UNSET in signatures."""
