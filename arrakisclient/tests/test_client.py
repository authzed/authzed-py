import asyncio

import pytest
from mock import AsyncMock

import authzed.api.v0.acl_service_pb2 as acl_proto
import authzed.api.v0.core_pb2 as core_proto
import authzed.api.v0.namespace_service_pb2 as ns_proto
from arrakisclient.client import ArrakisClient, AsyncArrakisClient, TuplesetFilter
from arrakisclient.test_util import (
    AsyncTestACLStub,
    AsyncTestNamespaceStub,
    mock_async_contextmanager,
)
from arrakisclient.types.namespace import ArrakisNamespace, Relation
from arrakisclient.types.tuple import ArrakisUserset, ObjectAndRelation


class _TestNS(ArrakisNamespace):
    __namespace__ = "test/namespace"

    bar1 = Relation(relation_name="bar1")
    bar2 = Relation(relation_name="bar2")
    auser = Relation(relation_name="auser")

    ellipsis = Relation(relation_name="...")


class _User(ArrakisNamespace):
    __namespace__ = "test/user"

    ellipsis = Relation(relation_name="...")


@pytest.fixture
def acl_stub() -> AsyncTestACLStub:
    return AsyncMock(spec=AsyncTestACLStub)


@pytest.fixture
def namespace_stub() -> AsyncTestNamespaceStub:
    return AsyncMock(spec=AsyncTestNamespaceStub)


@pytest.fixture
def client(acl_stub, namespace_stub) -> AsyncArrakisClient:
    client = AsyncArrakisClient(_TestNS, _User, endpoint="fakefakefake")
    client.acl_stub = mock_async_contextmanager(acl_stub)
    client.namespace_stub = mock_async_contextmanager(namespace_stub)
    return client


@pytest.fixture
def sync_client(acl_stub, namespace_stub) -> ArrakisClient:
    client = ArrakisClient(_TestNS, _User, endpoint="fakefakefake")
    client._delegate.acl_stub = mock_async_contextmanager(acl_stub)
    client._delegate.namespace_stub = mock_async_contextmanager(namespace_stub)
    return client


@pytest.mark.asyncio
async def test_check(client: AsyncArrakisClient, acl_stub: AsyncMock):
    acl_stub.Check = AsyncMock(
        return_value=acl_proto.CheckResponse(
            is_member=False,
            revision=core_proto.Zookie(token="123"),
            membership=acl_proto.CheckResponse.Membership.NOT_MEMBER,
        )
    )
    result = await client.check(
        _TestNS("mynamespace").ellipsis,
        ArrakisUserset.from_onr(_TestNS("myothernamespace").ellipsis),
    )
    assert not result.is_member
    assert result.revision.token == "123"


def test_check_sync(sync_client: ArrakisClient, acl_stub: AsyncTestACLStub):
    acl_stub.Check = AsyncMock(
        return_value=acl_proto.CheckResponse(
            is_member=False,
            revision=core_proto.Zookie(token="123"),
            membership=acl_proto.CheckResponse.Membership.NOT_MEMBER,
        )
    )
    result = sync_client.check(
        _TestNS("mynamespace").ellipsis,
        ArrakisUserset.from_onr(_TestNS("myothernamespace").ellipsis),
    )
    assert not result.is_member
    assert result.revision.token == "123"


@pytest.mark.asyncio
async def test_filter(client: AsyncArrakisClient, acl_stub: AsyncMock):
    acl_stub.Check = AsyncMock(
        return_value=acl_proto.CheckResponse(
            is_member=True,
            revision=core_proto.Zookie(token="123"),
            membership=acl_proto.CheckResponse.Membership.MEMBER,
        )
    )

    object_func = lambda x: _TestNS("myothernamespace").ellipsis
    user = ArrakisUserset.from_onr(_TestNS("myothernamespace").ellipsis)

    results = [
        item
        async for item in client.filter(
            object_id_func=object_func,
            items=["find me", "another item", "3", "4", "5", "6", "7", "8", "9", "10"],
            user=user,
            revision_func=lambda a: None,
        )
    ]

    assert results == ["find me", "another item", "3", "4", "5", "6", "7", "8", "9", "10"]


async def wait_on_second_call(request: acl_proto.CheckRequest):
    if request.test_userset.object_id == "another item":
        await asyncio.sleep(0.1)
    if request.test_userset.object_id == "filter me":
        return acl_proto.CheckResponse(
            is_member=False,
            revision=core_proto.Zookie(token="123"),
            membership=acl_proto.CheckResponse.Membership.NOT_MEMBER,
        )
    return acl_proto.CheckResponse(
        is_member=True,
        revision=core_proto.Zookie(token="123"),
        membership=acl_proto.CheckResponse.Membership.MEMBER,
    )


def test_filter_sync(sync_client: ArrakisClient, acl_stub: AsyncMock):
    acl_stub.Check = AsyncMock()
    acl_stub.Check.side_effect = wait_on_second_call

    object_func = lambda x: _TestNS(x).ellipsis
    user = ArrakisUserset.from_onr(_TestNS("myothernamespace").ellipsis)

    results = list(
        sync_client.filter(
            object_id_func=object_func,
            items=["find me", "another item", "3", "4", "5", "filter me", "7", "8", "9", "10"],
            user=user,
            revision_func=lambda a: None,
        )
    )

    assert results == ["find me", "another item", "3", "4", "5", "7", "8", "9", "10"]


@pytest.mark.asyncio
async def test_write(client: AsyncArrakisClient, acl_stub: AsyncMock):
    acl_stub.Write = AsyncMock(
        return_value=acl_proto.WriteResponse(revision=core_proto.Zookie(token="123"))
    )

    async with client.batch_write() as w:
        w.create(_TestNS("myothernamespace").ellipsis(_TestNS("mynamespace").ellipsis))

    assert w.revision.token == "123"


def test_write_sync(sync_client: ArrakisClient, acl_stub: AsyncMock):
    acl_stub.Write = AsyncMock(
        return_value=acl_proto.WriteResponse(revision=core_proto.Zookie(token="123"))
    )

    with sync_client.batch_write() as w:
        w.create(_TestNS("myothernamespace").ellipsis(_TestNS("mynamespace").ellipsis))

    assert w.revision.token == "123"


@pytest.mark.asyncio
async def test_write_namespace(client: AsyncArrakisClient, namespace_stub: AsyncMock):
    namespace_stub.WriteConfig = AsyncMock(
        return_value=ns_proto.WriteConfigResponse(revision=core_proto.Zookie(token="123"))
    )

    written = await client.management.write_namespace_configs(['name: "sharewith/resource"'])

    assert written.token == "123"


def test_write_namespace_sync(sync_client: ArrakisClient, namespace_stub: AsyncMock):
    namespace_stub.WriteConfig = AsyncMock(
        return_value=ns_proto.WriteConfigResponse(revision=core_proto.Zookie(token="123"))
    )

    written = sync_client.management.write_namespace_configs(['name: "sharewith/resource"'])

    assert written.token == "123"


@pytest.mark.asyncio
async def test_read(client: AsyncArrakisClient, acl_stub: AsyncMock):
    acl_stub.Read = AsyncMock(
        return_value=acl_proto.ReadResponse(
            tuplesets=[
                acl_proto.ReadResponse.Tupleset(
                    tuples=[
                        core_proto.RelationTuple(
                            object_and_relation=core_proto.ObjectAndRelation(
                                namespace="test/namespace",
                                relation="bar1",
                                object_id="baz",
                            ),
                            user=core_proto.User(
                                userset=core_proto.ObjectAndRelation(
                                    namespace="test/user", relation="...", object_id="1234"
                                )
                            ),
                        )
                    ]
                ),
                acl_proto.ReadResponse.Tupleset(
                    tuples=[
                        core_proto.RelationTuple(
                            object_and_relation=core_proto.ObjectAndRelation(
                                namespace="test/namespace",
                                relation="bar2",
                                object_id="baz2",
                            ),
                            user=core_proto.User(
                                userset=core_proto.ObjectAndRelation(
                                    namespace="test/namespace",
                                    relation="auser",
                                    object_id="hithere",
                                )
                            ),
                        )
                    ]
                ),
            ]
        )
    )

    result = await client.read(TuplesetFilter("test/namespace"), at_revision=None)
    tuples = list(result.tuples)
    assert tuples == [
        _TestNS("baz").bar1(ArrakisUserset.from_onr(ObjectAndRelation(_User("1234"), "..."))),
        _TestNS("baz2").bar2(
            ArrakisUserset.from_onr(ObjectAndRelation(_TestNS("hithere"), "auser"))
        ),
    ]


def test_read_sync(sync_client: ArrakisClient, acl_stub: AsyncMock):
    acl_stub.Read = AsyncMock(
        return_value=acl_proto.ReadResponse(
            tuplesets=[
                acl_proto.ReadResponse.Tupleset(
                    tuples=[
                        core_proto.RelationTuple(
                            object_and_relation=core_proto.ObjectAndRelation(
                                namespace="test/namespace",
                                relation="bar1",
                                object_id="baz",
                            ),
                            user=core_proto.User(
                                userset=core_proto.ObjectAndRelation(
                                    namespace="test/user", relation="...", object_id="1234"
                                )
                            ),
                        )
                    ]
                ),
                acl_proto.ReadResponse.Tupleset(
                    tuples=[
                        core_proto.RelationTuple(
                            object_and_relation=core_proto.ObjectAndRelation(
                                namespace="test/namespace",
                                relation="bar2",
                                object_id="baz2",
                            ),
                            user=core_proto.User(
                                userset=core_proto.ObjectAndRelation(
                                    namespace="test/namespace",
                                    relation="auser",
                                    object_id="hithere",
                                )
                            ),
                        )
                    ]
                ),
            ]
        )
    )

    result = sync_client.read(TuplesetFilter("test/namespace"), at_revision=None)
    tuples = list(result.tuples)
    assert tuples == [
        _TestNS("baz").bar1(ArrakisUserset.from_onr(ObjectAndRelation(_User("1234"), "..."))),
        _TestNS("baz2").bar2(
            ArrakisUserset.from_onr(ObjectAndRelation(_TestNS("hithere"), "auser"))
        ),
    ]
