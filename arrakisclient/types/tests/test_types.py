from typing import List, Set

import arrakisapi.api.core_pb2 as core_proto
import pytest

from arrakisclient.test_util import exclusion_proto, intersection_proto, leaf_proto, union_proto
from arrakisclient.types.expand import ExpandTree, _leaf_to_iterable
from arrakisclient.types.namespace import ArrakisNamespace, Relation, Self
from arrakisclient.types.tuple import ArrakisUser, ArrakisUserID


class UserGroup(ArrakisNamespace):
    __namespace__ = "sharewith/usergroup"

    manager = Relation(ArrakisUser, Self)
    member = Relation(ArrakisUser, Self)


class Resource(ArrakisNamespace):
    __namespace__ = "sharewith/resource"

    viewer = Relation(ArrakisUser, UserGroup)
    manager = Relation(ArrakisUser, UserGroup)


class Organization(ArrakisNamespace):
    __namespace__ = "sharewith/organization"

    group = Relation(UserGroup)
    member = Relation(ArrakisUser, UserGroup)
    admin = Relation(ArrakisUser, UserGroup)


NS_MAP = {ns.__namespace__: ns for ns in (UserGroup, Resource, Organization)}


@pytest.mark.parametrize(
    "obj,expected_repr",
    [
        (Organization("orgname"), "sharewith/organization:orgname"),
        (Organization("orgname").member, "sharewith/organization:orgname#member"),
        (
            Organization("orgname").member(ArrakisUserID(456)),
            "sharewith/organization:orgname#member@456",
        ),
        (
            Organization("orgname").member(UserGroup("owners").member),
            "sharewith/organization:orgname#member@sharewith/usergroup:owners#member",
        ),
    ],
)
def test_reprs(obj, expected_repr):
    assert repr(obj) == expected_repr


@pytest.mark.parametrize(
    "obj,expected_proto",
    [
        (
            Organization("orgname").member,
            core_proto.ObjectAndRelation(
                namespace="sharewith/organization",
                object_id="orgname",
                relation="member",
            ),
        ),
        (
            Organization("orgname").member(ArrakisUserID(456)),
            core_proto.RelationTuple(
                object_and_relation=core_proto.ObjectAndRelation(
                    namespace="sharewith/organization",
                    object_id="orgname",
                    relation="member",
                ),
                user=core_proto.User(user_id=456),
            ),
        ),
        (
            Organization("orgname").member(UserGroup("owners").member),
            core_proto.RelationTuple(
                object_and_relation=core_proto.ObjectAndRelation(
                    namespace="sharewith/organization",
                    object_id="orgname",
                    relation="member",
                ),
                user=core_proto.User(
                    userset=core_proto.ObjectAndRelation(
                        namespace="sharewith/usergroup",
                        object_id="owners",
                        relation="member",
                    ),
                ),
            ),
        ),
    ],
)
def test_protos(obj, expected_proto):
    assert obj.as_proto() == expected_proto


@pytest.mark.parametrize(
    "proto,expected_users",
    [
        (
            union_proto([leaf_proto([ArrakisUserID(1)])], Organization("petricorp").member),
            {ArrakisUserID(1)},
        ),
        (
            union_proto(
                [
                    leaf_proto([ArrakisUserID(1)]),
                    leaf_proto([ArrakisUserID(2)], onr=Organization("petricorp").admin),
                ],
                Organization("petricorp").member,
            ),
            {ArrakisUserID(1), ArrakisUserID(2)},
        ),
        (
            union_proto(
                [
                    union_proto(
                        [leaf_proto([ArrakisUserID(1)])],
                        Organization("petricorp").member,
                    ),
                    union_proto(
                        [leaf_proto([ArrakisUserID(2)])],
                        Organization("petricorp").member,  # This doesn't need to make sense
                    ),
                ],
                Organization("petricorp").admin,
            ),
            {ArrakisUserID(1), ArrakisUserID(2)},
        ),
        (
            intersection_proto(
                [
                    leaf_proto([ArrakisUserID(1)]),
                    union_proto(
                        [leaf_proto([ArrakisUserID(1)])],
                        Organization("petricorp").member,
                    ),
                    union_proto(
                        [leaf_proto([ArrakisUserID(1), ArrakisUserID(2)])],
                        Organization("petricorp").admin,
                    ),
                ],
                Organization("petricorp").admin,
            ),
            {ArrakisUserID(1)},
        ),
        (
            exclusion_proto(
                [
                    leaf_proto([ArrakisUserID(1), ArrakisUserID(2)]),
                    union_proto(
                        [leaf_proto([ArrakisUserID(1)])],
                        Organization("petricorp").member,
                    ),
                    union_proto(
                        [leaf_proto([ArrakisUserID(2)])],
                        Organization("petricorp").admin,
                    ),
                ],
                Organization("petricorp").member,
            ),
            set(),
        ),
        (
            union_proto(
                [
                    union_proto(
                        [leaf_proto([Organization("petricorp").member.as_userset()])],
                        Organization("petricorp").member,
                    ),
                    union_proto(
                        [leaf_proto([Organization("petricorp").admin.as_userset()])],
                        Organization("petricorp").admin,
                    ),
                ],
                Organization("petricorp").member,
            ),
            {
                Organization("petricorp").member.as_userset(),
                Organization("petricorp").admin.as_userset(),
            },
        ),
    ],
)
def test_flattened_children(
    proto: core_proto.RelationTupleTreeNode, expected_users: Set[ArrakisUserID]
):
    assert set(ExpandTree(proto, NS_MAP).flattened_children) == expected_users


@pytest.mark.parametrize(
    "proto,expected_users",
    [
        (
            leaf_proto([]),
            [],
        ),
        (
            leaf_proto([ArrakisUserID(1)]),
            [ArrakisUserID(1)],
        ),
        (
            leaf_proto(
                [
                    Organization("petricorp").member.as_userset(),
                    Organization("petricorp").admin.as_userset(),
                ]
            ),
            [
                Organization("petricorp").member.as_userset(),
                Organization("petricorp").admin.as_userset(),
            ],
        ),
    ],
)
def test_leaf_conversion(
    proto: core_proto.RelationTupleTreeNode, expected_users: List[ArrakisUserID]
):
    assert list(_leaf_to_iterable(proto.leaf_node, NS_MAP)) == expected_users


def test_direct_member_leaf_accessed_with_this():
    onr = Organization("petricorp").member
    example = ExpandTree(union_proto([leaf_proto([ArrakisUserID(1)])], onr), NS_MAP)
    assert list(example[onr.this_].leaf_children) == [ArrakisUserID(1)]

    # The parent ONR should not return the direct members, only a this_ should.
    with pytest.raises(KeyError):
        example[onr]
