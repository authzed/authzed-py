from asyncio import Future
from typing import AsyncContextManager, AsyncIterator, Callable, Iterable, TypeVar

from async_generator import asynccontextmanager
from typing_extensions import Protocol

import authzed.api.v0.acl_service_pb2 as acl_proto
import authzed.api.v0.core_pb2 as core_proto
import authzed.api.v0.namespace_service_pb2 as ns_proto
from arrakisclient.types.tuple import ArrakisUser, ObjectAndRelation


def leaf_proto(
    children: Iterable[ArrakisUser], onr: ObjectAndRelation = None
) -> core_proto.RelationTupleTreeNode:
    """
    Constructs a RelationTupleTreeNode Leaf protobuf message from client types.
    """
    onr_proto = core_proto.ObjectAndRelation() if onr is None else onr.as_proto()
    users = map(lambda x: x.as_proto(), children)
    return core_proto.RelationTupleTreeNode(
        leaf_node=core_proto.DirectUserset(users=users),
        expanded=onr_proto,
    )


def intermediate_proto(
    operation: core_proto.SetOperationUserset.Operation,
    children: Iterable[core_proto.RelationTupleTreeNode],
    onr: ObjectAndRelation,
) -> core_proto.RelationTupleTreeNode:
    return core_proto.RelationTupleTreeNode(
        intermediate_node=core_proto.SetOperationUserset(
            operation=operation,
            child_nodes=children,
        ),
        expanded=onr.as_proto(),
    )


def union_proto(
    children: Iterable[core_proto.RelationTupleTreeNode], onr: ObjectAndRelation
) -> core_proto.RelationTupleTreeNode:
    """
    Constructs a RelationTupleTreeNode Union protobuf message from client types.
    """
    return intermediate_proto(
        core_proto.SetOperationUserset.UNION,
        children,
        onr,
    )


def intersection_proto(
    children: Iterable[core_proto.RelationTupleTreeNode], onr: ObjectAndRelation
) -> core_proto.RelationTupleTreeNode:
    """
    Constructs a RelationTupleTreeNode Intersection protobuf message from client types.
    """
    return intermediate_proto(
        core_proto.SetOperationUserset.INTERSECTION,
        children,
        onr,
    )


def exclusion_proto(
    children: Iterable[core_proto.RelationTupleTreeNode], onr: ObjectAndRelation
) -> core_proto.RelationTupleTreeNode:
    """
    Constructs a RelationTupleTreeNode Exclusion protobuf message from client types.
    """
    return intermediate_proto(
        core_proto.SetOperationUserset.EXCLUSION,
        children,
        onr,
    )


class AsyncTestACLStub(Protocol):
    """ Stub which can be used as a spec for mocking out the ACL stub in a client. """

    def Read(self, req: acl_proto.ReadRequest) -> "Future[acl_proto.ReadResponse]":
        ...

    def Write(self, req: acl_proto.WriteRequest) -> "Future[acl_proto.WriteResponse]":
        ...

    def Check(self, req: acl_proto.CheckRequest) -> "Future[acl_proto.CheckResponse]":
        ...

    def ContentChangeCheck(
        self, req: acl_proto.ContentChangeCheckRequest
    ) -> "Future[acl_proto.CheckResponse]":
        ...

    def Expand(self, req: acl_proto.ExpandRequest) -> "Future[acl_proto.ExpandResponse]":
        ...


class AsyncTestNamespaceStub(Protocol):
    """ Stub which can be used as a spec for mocking out the Namespace stub in a client. """

    def ReadConfig(self, req: ns_proto.ReadConfigRequest) -> "Future[ns_proto.ReadConfigResponse]":
        ...

    def WriteConfig(
        self, req: ns_proto.WriteConfigRequest
    ) -> "Future[ns_proto.WriteConfigResponse]":
        ...


T = TypeVar("T")


def mock_async_contextmanager(to_return: T) -> Callable[[], AsyncContextManager[T]]:
    """This mock async context manager generator can be bound to an AsyncMock to mock the way
    the arrakis client makes calls to the underlying service."""

    @asynccontextmanager
    async def inner() -> AsyncIterator[T]:
        yield to_return

    return inner
