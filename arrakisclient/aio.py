import asyncio
import logging
from dataclasses import dataclass
from itertools import islice
from typing import AsyncIterator, Callable, Dict, Iterable, Iterator, List, Optional
from typing import Tuple as TupleType
from typing import Type, TypeVar, Union

import grpc
import grpc.aio
from async_generator import asynccontextmanager

import authzed.api.v0.acl_service_pb2 as acl_proto
import authzed.api.v0.acl_service_pb2_grpc as acl_grpc_proto
import authzed.api.v0.core_pb2 as core_proto
import authzed.api.v0.namespace_service_pb2 as ns_service_proto
import authzed.api.v0.namespace_service_pb2_grpc as ns_grpc_proto
from arrakisclient.types.errors import RequestException, wrap_client_exception_async
from arrakisclient.types.expand import ExpandTree
from arrakisclient.types.namespace import ArrakisNamespace, Relation
from arrakisclient.types.parsers import parse_namespace_config
from arrakisclient.types.tuple import ArrakisUser, ObjectAndRelation, Tuple
from arrakisclient.types.zookie import Zookie


class TuplesetFilter(object):
    """TuplesetFilter defines a filter for reading tuples using the ArrakisClient.read() method.
    All filters are optional except for the namespace."""

    def __init__(
        self,
        namespace: str,
        object_id: Optional[str] = None,
        relation: Optional[str] = None,
        userset: Optional[ObjectAndRelation] = None,
    ):
        self.namespace = namespace
        self.object_id = object_id
        self.relation = relation
        self.userset = userset

    @classmethod
    def for_relation(cls, namespace: Type[ArrakisNamespace], relation: Relation):
        return TuplesetFilter(namespace.__namespace__, relation=relation.relation_name)

    def with_object_id(self, object_id: str) -> "TuplesetFilter":
        return self._clone(object_id=object_id)

    def with_relation(self, relation: str) -> "TuplesetFilter":
        return self._clone(relation=relation)

    def with_userset(self, userset: ObjectAndRelation) -> "TuplesetFilter":
        return self._clone(userset=userset)

    def as_proto(self) -> acl_proto.RelationTupleFilter:
        filters = []
        if self.object_id:
            filters.append(acl_proto.RelationTupleFilter.OBJECT_ID)

        if self.relation:
            filters.append(acl_proto.RelationTupleFilter.RELATION)

        if self.userset:
            filters.append(acl_proto.RelationTupleFilter.USERSET)

        return acl_proto.RelationTupleFilter(
            namespace=self.namespace,
            filters=filters,
            object_id=self.object_id or None,
            relation=self.relation or None,
            userset=self.userset.as_proto() if self.userset else None,
        )

    def _clone(self, object_id=None, relation=None, user_id=None, userset=None) -> "TuplesetFilter":
        return TuplesetFilter(
            self.namespace,
            object_id=object_id or self.object_id,
            relation=relation or self.relation,
            userset=userset or self.userset,
        )


class CheckResponse(object):
    """CheckResponse object for a call to ArrakisClient.check() or
    ArrakisClient.content_change_check(). Implements __bool__ so that the response object can be
    used as a truthy or falsy value directly, indicating relation membership.
    """

    def __init__(self, check_response: acl_proto.CheckResponse):
        self._check_response_proto = check_response

    @property
    def is_member(self) -> bool:
        return self._check_response_proto.membership == acl_proto.CheckResponse.Membership.MEMBER

    def __bool__(self) -> bool:
        return self.is_member

    @property
    def revision(self) -> Zookie:
        return Zookie(self._check_response_proto.revision)


@dataclass
class ExpandResponse(object):
    expansion: ExpandTree
    revision: Optional[Zookie]

    @classmethod
    def from_proto(
        cls, pb: acl_proto.ExpandResponse, ns_map: Dict[str, Type[ArrakisNamespace]]
    ) -> "ExpandResponse":
        return ExpandResponse(
            ExpandTree(
                pb.tree_node,
                ns_map,
                ObjectAndRelation.from_proto(pb.tree_node.expanded, ns_map),
            ),
            Zookie.from_token(pb.revision.token),
        )


@dataclass
class LookupResponse(object):
    resolved_object_ids: Iterable[str]
    next_page_reference: str
    revision: Zookie

    @classmethod
    def from_proto(cls, pb: acl_proto.LookupResponse) -> "LookupResponse":
        return LookupResponse(
            pb.resolved_object_ids,
            pb.next_page_reference,
            Zookie.from_token(pb.revision.token),
        )


class ReadResponse(object):
    def __init__(
        self, read_response: acl_proto.ReadResponse, ns_map: Dict[str, Type[ArrakisNamespace]]
    ):
        self._read_response_proto = read_response
        self._ns_map = ns_map

    @property
    def tuples(self) -> Iterator[Tuple]:
        for tupleset in self._read_response_proto.tuplesets:
            yield from [Tuple.from_proto(tpl_proto, self._ns_map) for tpl_proto in tupleset.tuples]

    @property
    def revision(self) -> Zookie:
        return Zookie(self._read_response_proto.revision)

    @classmethod
    def from_proto(
        cls, pb: acl_proto.ReadResponse, ns_map: Dict[str, Type[ArrakisNamespace]]
    ) -> "ReadResponse":
        return ReadResponse(pb, ns_map)


T = TypeVar("T")


def build_grpc_credentials(
    *, insecure: bool, tls_cert: Optional[bytes], access_token: Optional[str]
):
    """ Builds the GRPC credentials for a combination of the TLS cert, access token and insecure. """
    if insecure:
        credentials = grpc.local_channel_credentials(grpc.LocalConnectionType.LOCAL_TCP)
    else:
        credentials = grpc.ssl_channel_credentials(root_certificates=tls_cert)

    if access_token is not None:
        call_credentials = grpc.access_token_call_credentials(access_token)
        credentials = grpc.composite_channel_credentials(credentials, call_credentials)

    return credentials


class AsyncArrakisClient(object):
    """Asynchronous (asyncio) Python client for communicating with Authzed."""

    class AsyncWriteOperation(object):
        """ Async ContextManager which is used to send a batch of mutations to the server. """

        def __init__(
            self,
            client: "AsyncArrakisClient",
            preconditions: Iterable[Tuple],
        ):
            self._client = client
            tuple_preconditions = map(lambda tpl: tpl.as_proto(), preconditions)
            self._request = acl_proto.WriteRequest(write_conditions=tuple_preconditions)
            self._response_proto = None

        async def __aenter__(self) -> "AsyncArrakisClient.AsyncWriteOperation":
            assert self._response_proto is None, "cannot re-enter previously executed write op"
            return self

        def _update(
            self, operation: "core_proto.RelationTupleUpdate.OperationValue", tpls: Iterable[Tuple]
        ):
            self._request.updates.extend(
                [
                    core_proto.RelationTupleUpdate(operation=operation, tuple=tpl.as_proto())
                    for tpl in tpls
                ]
            )

        def create(self, *tpls: Tuple):
            """ Create new tuple(s). """
            assert self._response_proto is None, "cannot modify previously executed write op"
            self._update(core_proto.RelationTupleUpdate.Operation.CREATE, tpls)

        def delete(self, *tpls: Tuple):
            """ Delete existing tuple(s). """
            assert self._response_proto is None, "cannot modify previously executed write op"
            self._update(core_proto.RelationTupleUpdate.Operation.DELETE, tpls)

        def touch(self, *tpls: Tuple):
            """ Touch, i.e. upsert tuple(s). """
            assert self._response_proto is None, "cannot modify previously executed write op"
            self._update(core_proto.RelationTupleUpdate.Operation.TOUCH, tpls)

        @property
        def revision(self) -> Zookie:
            """After executing the write operation, return the revision at which the write has
            occurred."""
            assert (
                self._response_proto is not None
            ), "revision doesn't exist for an unexecuted write op"
            return Zookie(self._response_proto.revision)

        @wrap_client_exception_async
        async def __aexit__(self, exc_type, exc_value, traceback) -> bool:
            if exc_type is not None:
                # We return False here to allow the exception to propagate
                return False

            async with self._client.acl_stub() as acl_stub:
                self._response_proto = await acl_stub.Write(self._request)
                return True

    class AsyncTenantManagementClient(object):
        """Async client which is used for tenant management operations, such as updating namespace
        config."""

        def __init__(self, client: "AsyncArrakisClient"):
            self._client = client

        @wrap_client_exception_async
        async def write_namespace_configs(self, configs: List[str]) -> Zookie:
            assert len(configs), "Missing namespace config"

            async with self._client.namespace_stub() as ns_stub:
                namespace_definitions = [parse_namespace_config(config) for config in configs]
                written: ns_service_proto.WriteConfigResponse = await ns_stub.WriteConfig(
                    ns_service_proto.WriteConfigRequest(configs=namespace_definitions)
                )
                return Zookie(written.revision)

    def __init__(
        self,
        *namespace_types: Type[ArrakisNamespace],
        endpoint: str = "grpc.authzed.com:443",
        insecure: bool = False,
        tls_cert: Optional[bytes] = None,
        access_token: Optional[str] = None,
    ):
        credentials = build_grpc_credentials(
            insecure=insecure, tls_cert=tls_cert, access_token=access_token
        )

        self._endpoint = endpoint
        self._credentials = credentials
        self._ns_map = {ns.__namespace__: ns for ns in namespace_types}
        self._management_client = AsyncArrakisClient.AsyncTenantManagementClient(self)

    async def filter(
        self,
        *,
        object_id_func: Callable[[T], ObjectAndRelation],
        items: Union[Iterator[T], Iterable[T]],
        user: ArrakisUser,
        revision_func: Callable[[T], Optional[Zookie]] = lambda x: None,
        use_content_change_check: bool = False,
    ) -> AsyncIterator[T]:
        """Takes an iterable, and functions which transform that iterable into checkable objects,
        and returns a filtered iterable which contains only the objects for which the user has the
        specified relation."""
        async for item in self.filter_with_user_func(
            object_id_func=object_id_func,
            items=items,
            user_func=lambda x: user,
            revision_func=revision_func,
            use_content_change_check=use_content_change_check,
        ):
            yield item

    async def filter_with_user_func(
        self,
        *,
        object_id_func: Callable[[T], ObjectAndRelation],
        items: Union[Iterator[T], Iterable[T]],
        user_func: Callable[[T], ArrakisUser],
        revision_func: Callable[[T], Optional[Zookie]] = lambda x: None,
        use_content_change_check: bool = False,
    ) -> AsyncIterator[T]:
        """Takes an iterable, and functions which transform that iterable into checkable objects,
        and return a filtered iterable which contains only the objects for which the user (as
        computed by the user_func argument) has the specified relation."""

        loop = asyncio.get_event_loop()

        def request_func(item: T) -> "TupleType[T, asyncio.Task[CheckResponse]]":
            if use_content_change_check:
                return (
                    item,
                    loop.create_task(
                        self.content_change_check(object_id_func(item), user_func(item))
                    ),
                )

            return (
                item,
                loop.create_task(
                    self.check(object_id_func(item), user_func(item), revision_func(item))
                ),
            )

        futures_iter = map(request_func, iter(items))

        batch_size = 8
        more_items = True
        while more_items:
            batch = list(islice(futures_iter, batch_size))
            for item, future in batch:
                try:
                    check_response = await future
                    if check_response.is_member:
                        yield item
                except RequestException as re:
                    # If we passed a bad check request we consider it a failed auth check
                    # (e.g. check of a relationship with a cycle)
                    if re.code() == grpc.StatusCode.INVALID_ARGUMENT:
                        logging.exception("Invalid check request")
                        continue

                    # Otherwise, raise as an error.
                    raise

            more_items = len(batch) == batch_size

            # TODO consider adding a max batch size config option or fixed limit
            batch_size *= 2

    @wrap_client_exception_async
    async def check(
        self,
        onr: ObjectAndRelation,
        user: ArrakisUser,
        at_revision: Optional[Zookie] = None,
    ) -> CheckResponse:
        """ Check if the specified user has the specified relation. """
        async with self.acl_stub() as acl_stub:
            zookie_proto = at_revision and at_revision.zookie_proto
            raw_response = await acl_stub.Check(
                acl_proto.CheckRequest(
                    test_userset=onr.as_proto(),
                    user=user.as_proto(),
                    at_revision=zookie_proto,
                )
            )
            return CheckResponse(raw_response)

    @wrap_client_exception_async
    async def content_change_check(
        self, onr: ObjectAndRelation, user: ArrakisUser
    ) -> CheckResponse:
        """Check that the specified user has the specified relation at a revision which encompasses
        all changes up through at least the current time."""
        async with self.acl_stub() as acl_stub:
            raw_response = await acl_stub.ContentChangeCheck(
                acl_proto.ContentChangeCheckRequest(
                    test_userset=onr.as_proto(),
                    user=user.as_proto(),
                )
            )
            return CheckResponse(raw_response)

    @wrap_client_exception_async
    async def expand(
        self, onr: ObjectAndRelation, at_revision: Optional[Zookie] = None
    ) -> ExpandResponse:
        """Expand the specified object and relation to create a tree of all referenced objects,
        and their sub-relationships, recursively."""
        async with self.acl_stub() as acl_stub:
            zookie_proto = at_revision and at_revision.zookie_proto
            raw_response = await acl_stub.Expand(
                acl_proto.ExpandRequest(
                    userset=onr.as_proto(),
                    at_revision=zookie_proto,
                )
            )
            return ExpandResponse.from_proto(raw_response, self._ns_map)

    @wrap_client_exception_async
    async def lookup(
        self,
        namespace: str,
        relation: str,
        user: ArrakisUser,
        at_revision: Optional[Zookie] = None,
        page_ref: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> LookupResponse:
        async with self.acl_stub() as acl_stub:
            zookie_proto = at_revision and at_revision.zookie_proto
            raw_response = await acl_stub.Lookup(
                acl_proto.LookupRequest(
                    object_relation=core_proto.RelationReference(
                        namespace=namespace,
                        relation=relation,
                    ),
                    user=user.as_proto().userset,
                    at_revision=zookie_proto,
                    page_reference=page_ref or "",
                    limit=limit or 0,
                )
            )
            return LookupResponse.from_proto(raw_response)

    @wrap_client_exception_async
    async def read(
        self, *tupleset_filters: TuplesetFilter, at_revision: Optional[Zookie]
    ) -> ReadResponse:
        """ Reads the full sets of tuples matching the given tuplesets. """
        async with self.acl_stub() as acl_stub:
            zookie_proto = at_revision and at_revision.zookie_proto
            raw_response = await acl_stub.Read(
                acl_proto.ReadRequest(
                    tuplesets=[f.as_proto() for f in tupleset_filters],
                    at_revision=zookie_proto,
                )
            )
            return ReadResponse.from_proto(raw_response, self._ns_map)

    @asynccontextmanager
    async def acl_stub(self) -> AsyncIterator[acl_grpc_proto.ACLServiceStub]:
        """Async ContextManager which allocates a client which can be used to talk to the upstream
        ACL service while in the context."""
        async with grpc.aio.secure_channel(self._endpoint, self._credentials) as channel:
            yield acl_grpc_proto.ACLServiceStub(channel)

    @asynccontextmanager
    async def namespace_stub(self) -> AsyncIterator[ns_grpc_proto.NamespaceServiceStub]:
        """Async ContextManager which allocates a client which can be used to talk to the upstream
        Namespace service while in the context."""
        async with grpc.aio.secure_channel(self._endpoint, self._credentials) as channel:
            yield ns_grpc_proto.NamespaceServiceStub(channel)

    @property
    def management(self) -> "AsyncArrakisClient.AsyncTenantManagementClient":
        """Returns a client that can be used to perform tenant management operations such as
        updating a namespace."""
        return self._management_client

    def batch_write(self, preconditions: Iterable[Tuple] = []) -> AsyncWriteOperation:
        """ Start a new batch write operation. """
        return AsyncArrakisClient.AsyncWriteOperation(self, preconditions)
