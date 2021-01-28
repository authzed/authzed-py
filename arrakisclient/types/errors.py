from functools import wraps
from typing import Any, Callable, Optional, TypeVar

import grpc
import grpc.aio


class RequestException(Exception):
    """An exception was raised when communicating with the service."""

    def __init__(self, delegate: grpc.aio.AioRpcError):
        self._delegate = delegate

    grpc.aio._call.AioRpcError

    def code(self) -> grpc.StatusCode:
        return self._delegate.code()

    def details(self) -> Optional[str]:
        return self._delegate.details()

    def debug_error_string(self) -> str:
        return self._delegate.debug_error_string()


T = TypeVar("T", bound=Callable[..., Any])


def wrap_client_exception_async(f: T) -> T:
    """Decorator which will intercept exceptions coming from the server and
    rewrite them into a usable format.
    """

    @wraps(f)
    async def inner(*args, **kwargs):
        try:
            return await f(*args, **kwargs)
        except grpc.aio.AioRpcError as rpce:
            raise RequestException(rpce)

    return inner
