from __future__ import annotations

from typing import Dict, Generic, Optional, Type, TypeVar


class Namespace:
    _name_: str

    def __init__(self, object_id: str):
        self._object_id = object_id

    @classmethod
    def _annotations(cls) -> Dict[str, str]:
        annotations = {}
        for c in reversed(cls.mro()):
            try:
                annotations.update(**c.__annotations__)
            except AttributeError:
                pass
        return annotations

    def __getattr__(self, name):
        annotated_type = self._annotations().get(name, None)
        if annotated_type == ObjectAndRelation.__name__:
            return ObjectAndRelation(self, name)

        raise AttributeError()

    def __repr__(self) -> str:
        return f"{self._name_}:{self._object_id}"


T = TypeVar("T", bound=Namespace)


def relation(relation_name: Optional[str] = None) -> ObjectAndRelation:
    return ObjectAndRelation(relation_name)


class ObjectAndRelation(Generic[T]):
    def __init__(self, relation_name: Optional[str], object: Optional[Namespace] = None):
        self._object = None
        self._relation_name = relation_name

    def bind(object: Namespace) -> ObjectAndRelation:
        return ObjectAndRelation

    @property
    def relation(self) -> Optional[str]:
        return self._relation_name

    def __call__(self, userset: ObjectAndRelation[T]) -> Tuple:
        return Tuple(self, userset)

    def __repr__(self) -> str:
        return f"{self._object}#{self._relation_name}"


class Tuple:
    def __init__(self, object_and_relation: ObjectAndRelation, userset: ObjectAndRelation):
        self._object_and_relation = object_and_relation
        self._userset = userset

    def __repr__(self) -> str:
        return f"{self._object_and_relation}@{self._userset}"


class ReferenceableNamespace(Namespace):
    ellipsis: ObjectAndRelation


class User(ReferenceableNamespace):
    _name_ = "juniper/user"


class Group(ReferenceableNamespace):
    _name_ = "juniper/usergroup"

    member: ObjectAndRelation[User]


class ViewAndEditable(Namespace):
    view: ObjectAndRelation[Group]
    edit: ObjectAndRelation[Group]


class Document(ViewAndEditable):
    _name_ = "juniper/document"


secret = Document("secretdoc")
doc = User("specialist")
patient = User("bill")
doctors = Group("doctors")

import ipdb

ipdb.set_trace()

secret.view(doctors.ellipsis)
secret.edit(doctors.ellipsis)

doctors.member(doc.ellipsis)
