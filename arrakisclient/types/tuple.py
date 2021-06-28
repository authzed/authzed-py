from copy import copy
from typing import TYPE_CHECKING, Dict, Type

import authzed.api.v0.core_pb2 as core_proto

if TYPE_CHECKING:
    from arrakisclient.types.namespace import ArrakisNamespace


class ObjectAndRelation(object):
    """ Represents a namespace, object ID, and relation bound into a single value. """

    def __init__(self, obj: "ArrakisNamespace", relation_name: str):
        self._obj = obj
        self._relation_name = relation_name
        self._this = False

    def __call__(self, userset: "ObjectAndRelation") -> "Tuple":
        return Tuple(self, ArrakisUserset.from_onr(userset))

    def __repr__(self) -> str:
        return f"{self._obj}#{self._relation_name}"

    @property
    def object_id(self) -> str:
        return self._obj.object_id

    @property
    def object(self) -> "ArrakisNamespace":
        return self._obj

    @property
    def relation(self) -> str:
        return self._relation_name

    def as_proto(self) -> core_proto.ObjectAndRelation:
        return core_proto.ObjectAndRelation(
            namespace=self._obj.namespace,
            object_id=self._obj.object_id,
            relation=self._relation_name,
        )

    @classmethod
    def from_proto(
        cls, pb: core_proto.ObjectAndRelation, ns_map: Dict[str, Type["ArrakisNamespace"]]
    ):
        obj = ns_map[pb.namespace](pb.object_id)
        return obj.relation(pb.relation)

    def __eq__(self, other: "ObjectAndRelation") -> bool:
        return (
            self._obj == other._obj
            and self._relation_name == other._relation_name
            and self._this == other._this
        )

    def as_userset(self) -> "ArrakisUserset":
        return ArrakisUserset.from_onr(self)

    def __hash__(self):
        return hash(repr(self))

    @property
    def this_(self) -> "ObjectAndRelation":
        this = copy(self)
        this._this = True
        return this


class ArrakisUserset(ObjectAndRelation):
    def as_proto(self) -> core_proto.User:
        return core_proto.User(userset=super().as_proto())

    @classmethod
    def from_onr(cls, onr: ObjectAndRelation) -> "ArrakisUserset":
        return cls(onr._obj, onr._relation_name)


ArrakisUser = ArrakisUserset


class Tuple(object):
    """ Represents the binding of an ObjectAndRelation to a specific user or userset. """

    def __init__(self, onr: ObjectAndRelation, user: ArrakisUser):
        self._onr = onr
        self._user = user

    @classmethod
    def from_proto(
        cls, tuple_proto: core_proto.RelationTuple, ns_map: Dict[str, Type["ArrakisNamespace"]]
    ) -> "Tuple":
        user = ArrakisUserset.from_onr(
            ObjectAndRelation.from_proto(tuple_proto.user.userset, ns_map)
        )
        return Tuple(ObjectAndRelation.from_proto(tuple_proto.object_and_relation, ns_map), user)

    def __repr__(self) -> str:
        return f"{self._onr}@{self._user}"

    def as_proto(self) -> core_proto.RelationTuple:
        return core_proto.RelationTuple(
            object_and_relation=self._onr.as_proto(), user=self._user.as_proto()
        )

    def __eq__(self, other: "Tuple") -> bool:
        return self._onr == other._onr and self._user == other._user

    def __hash__(self):
        return hash(repr(self))

    @property
    def onr(self) -> ObjectAndRelation:
        return self._onr

    @property
    def user(self) -> ArrakisUser:
        return self._user
