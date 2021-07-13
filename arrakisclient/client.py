import asyncio
from typing import Awaitable, Callable, Iterable, Iterator, List, Optional, Type, TypeVar, Union

from arrakisclient.aio import (
    AsyncArrakisClient,
    CheckResponse,
    ExpandResponse,
    LookupResponse,
    ReadResponse,
    TuplesetFilter,
)
from arrakisclient.types.namespace import ArrakisNamespace
from arrakisclient.types.tuple import ArrakisUser, ObjectAndRelation, Tuple
from arrakisclient.types.zookie import Zookie

U = TypeVar("U")


def _aio_run(coro: Awaitable[U]) -> U:
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coro)


T = TypeVar("T")


class ArrakisClient(object):
    """Synchronous Python client for communicating with Authzed."""

    class WriteOperation(AsyncArrakisClient.AsyncWriteOperation):
        def __init__(self, client: AsyncArrakisClient, preconditions: Iterable[Tuple]):
            super().__init__(client, preconditions)

        def __enter__(self) -> AsyncArrakisClient.AsyncWriteOperation:
            assert self._response_proto is None, "cannot re-enter previously executed write op"
            return self

        def __exit__(self, exc_type, exc_value, traceback) -> bool:
            return _aio_run(super().__aexit__(exc_type, exc_value, traceback))

    class TenantManagementClient:
        def __init__(self, delegate: AsyncArrakisClient.AsyncTenantManagementClient):
            self._delegate = delegate

        def write_namespace_configs(self, configs: List[str]) -> Zookie:
            return _aio_run(self._delegate.write_namespace_configs(configs))

    def __init__(
        self,
        *namespace_types: Type[ArrakisNamespace],
        endpoint: str = "grpc.authzed.com:443",
        insecure: bool = False,
        tls_cert: bytes = None,
        access_token: str = None,
    ):
        self._delegate = AsyncArrakisClient(
            *namespace_types,
            endpoint=endpoint,
            insecure=insecure,
            tls_cert=tls_cert,
            access_token=access_token,
        )
        self._management = self.TenantManagementClient(self._delegate.management)

    def filter(
        self,
        *,
        object_id_func: Callable[[T], ObjectAndRelation],
        items: Union[Iterator[T], Iterable[T]],
        user: ArrakisUser,
        revision_func: Callable[[T], Optional[Zookie]] = lambda x: None,
    ) -> Iterator[T]:
        yield from self.filter_with_user_func(
            object_id_func=object_id_func,
            items=items,
            user_func=lambda x: user,
            revision_func=revision_func,
        )

    def filter_with_user_func(
        self,
        *,
        object_id_func: Callable[[T], ObjectAndRelation],
        items: Union[Iterator[T], Iterable[T]],
        user_func: Callable[[T], ArrakisUser],
        revision_func: Callable[[T], Optional[Zookie]] = lambda x: None,
    ) -> Iterator[T]:
        response_iter = self._delegate.filter_with_user_func(
            object_id_func=object_id_func,
            items=items,
            user_func=user_func,
            revision_func=revision_func,
        )

        loop = asyncio.new_event_loop()

        try:
            while True:
                yield loop.run_until_complete(response_iter.__anext__())
        except StopAsyncIteration:
            return

    def check(
        self,
        onr: ObjectAndRelation,
        user: ArrakisUser,
        at_revision: Optional[Zookie] = None,
    ) -> CheckResponse:
        return _aio_run(self._delegate.check(onr, user, at_revision))

    def content_change_check(self, onr: ObjectAndRelation, user: ArrakisUser) -> CheckResponse:
        return _aio_run(self._delegate.content_change_check(onr, user))

    def read(
        self, *tupleset_filters: TuplesetFilter, at_revision: Optional[Zookie]
    ) -> ReadResponse:
        return _aio_run(self._delegate.read(*tupleset_filters, at_revision=at_revision))

    def expand(
        self, onr: ObjectAndRelation, at_revision: Optional[Zookie] = None
    ) -> ExpandResponse:
        return _aio_run(self._delegate.expand(onr, at_revision))

    def lookup(
        self,
        namespace: str,
        relation: str,
        user: ArrakisUser,
        at_revision: Optional[Zookie] = None,
        page_ref: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> LookupResponse:
        return _aio_run(
            self._delegate.lookup(namespace, relation, user, at_revision, page_ref, limit)
        )

    @property
    def management(self) -> "ArrakisClient.TenantManagementClient":
        """Returns a client that can be used to perform tenant management operations such as
        updating a namespace."""
        return self._management

    def batch_write(self, preconditions: Iterable[Tuple] = []) -> WriteOperation:
        return ArrakisClient.WriteOperation(self._delegate, preconditions)
