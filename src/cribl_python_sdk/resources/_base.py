"""Base resource class with cast_to response parsing."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Literal, TypeVar

from pydantic import BaseModel

from .._response import SDKResponse
from ..exceptions import ResponseValidationError

if TYPE_CHECKING:
    from ..client import Cribl

ModelT = TypeVar("ModelT", bound=BaseModel)


class BaseResource:
    _surface: ClassVar[Literal["control_plane", "cloud"]] = "control_plane"

    def __init__(self, client: Cribl):
        self._client = client

    def _parse(self, resp: Any, cast_to: type[ModelT]) -> SDKResponse[ModelT]:
        data = resp.json() if resp.content else None
        try:
            parsed = cast_to.model_validate(data)
        except Exception as exc:
            raise ResponseValidationError(
                url=str(resp.url),
                status_code=resp.status_code,
                body=resp.text,
                original=exc,
            ) from exc
        return SDKResponse(
            data=parsed,
            status_code=resp.status_code,
            headers=resp.headers,
            raw_response=resp,
        )

    def _get(self, path: str, *, cast_to: type[ModelT], params: dict[str, Any] | None = None, **kwargs: Any) -> SDKResponse[ModelT]:
        return self._parse(self._client._request("GET", path, surface=self._surface, params=params, **kwargs), cast_to)

    async def _get_async(self, path: str, *, cast_to: type[ModelT], params: dict[str, Any] | None = None, **kwargs: Any) -> SDKResponse[ModelT]:
        return self._parse(await self._client._request_async("GET", path, surface=self._surface, params=params, **kwargs), cast_to)

    def _post(self, path: str, *, cast_to: type[ModelT], json: Any = None, **kwargs: Any) -> SDKResponse[ModelT]:
        return self._parse(self._client._request("POST", path, surface=self._surface, json=json, **kwargs), cast_to)

    async def _post_async(self, path: str, *, cast_to: type[ModelT], json: Any = None, **kwargs: Any) -> SDKResponse[ModelT]:
        return self._parse(await self._client._request_async("POST", path, surface=self._surface, json=json, **kwargs), cast_to)

    def _patch(self, path: str, *, cast_to: type[ModelT], json: Any = None, **kwargs: Any) -> SDKResponse[ModelT]:
        return self._parse(self._client._request("PATCH", path, surface=self._surface, json=json, **kwargs), cast_to)

    async def _patch_async(self, path: str, *, cast_to: type[ModelT], json: Any = None, **kwargs: Any) -> SDKResponse[ModelT]:
        return self._parse(await self._client._request_async("PATCH", path, surface=self._surface, json=json, **kwargs), cast_to)

    def _put(self, path: str, *, cast_to: type[ModelT], **kwargs: Any) -> SDKResponse[ModelT]:
        return self._parse(self._client._request("PUT", path, surface=self._surface, **kwargs), cast_to)

    async def _put_async(self, path: str, *, cast_to: type[ModelT], **kwargs: Any) -> SDKResponse[ModelT]:
        return self._parse(await self._client._request_async("PUT", path, surface=self._surface, **kwargs), cast_to)

    def _delete(self, path: str, *, cast_to: type[ModelT], **kwargs: Any) -> SDKResponse[ModelT]:
        return self._parse(self._client._request("DELETE", path, surface=self._surface, **kwargs), cast_to)

    async def _delete_async(self, path: str, *, cast_to: type[ModelT], **kwargs: Any) -> SDKResponse[ModelT]:
        return self._parse(await self._client._request_async("DELETE", path, surface=self._surface, **kwargs), cast_to)
