import copy
from typing import List, Optional, Type, Union

from arrakisclient.types.tuple import ArrakisUserset, ObjectAndRelation, Tuple
from arrakisclient.validation import validate_namespace_name, validate_relation_name


class Self(object):
    pass


# We set the parent class here ONLY to make the type checker happy
class Relation(ObjectAndRelation):
    """ Declarative namespace config class for representing an authorization server relation. """

    def __init__(
        self,
        *relates_to_types: Union[
            Type["ArrakisNamespace"],
            Type[ArrakisUserset],
            Type[Self],
        ],
        relation_name=None,
    ):
        self._relates_to_types = relates_to_types
        self._relation_name = relation_name
        self._parent_class_name = None
        self._attr_key = relation_name

    def __call__(self, userset: ObjectAndRelation) -> Tuple:
        raise RuntimeError("Cannot call an unbound relation")

    def __repr__(self) -> str:
        if self.parent_class_name is not None:
            return f"{ self.parent_class_name }#{ self.relation_name }"
        return self.relation_name

    @property
    def relation_name(self) -> str:
        return self._relation_name

    @relation_name.setter
    def relation_name(self, relation_name: str):
        self._relation_name = relation_name

    @property
    def parent_class_name(self) -> "Optional[str]":
        return self._parent_class_name

    def _set_parent_class_name(self, parent_class: str):
        self._parent_class_name = parent_class

    def __eq__(self, other: "Relation") -> bool:
        return id(self) == id(other)

    def __hash__(self):
        return hash(self._relation_name) ^ hash(self.parent_class_name)


class _ArrakisNamespaceMeta(type):
    def __new__(cls, name, bases, attrs):
        if attrs.get("__namespace__", "") != "":
            if not validate_namespace_name(attrs.get("__namespace__")):
                raise RuntimeError("Invalid namespace name: %s" % attrs.get("__namespace__"))

        # Copy over inherited relationship attrs
        for base in bases:
            for attr_name, attr_value in vars(base).items():
                if isinstance(attr_value, Relation) and attr_name not in attrs:
                    attrs[attr_name] = copy.copy(attr_value)

        relations = []
        for attr_key, attr_value in attrs.items():
            if isinstance(attr_value, Relation):
                attr_value._set_parent_class_name(name)

                attr_value._attr_key = attr_key
                if attr_value.relation_name is None:
                    attr_value.relation_name = attr_key

                if not validate_relation_name(attr_value.relation_name):
                    raise RuntimeError("Invalid relation name: %s" % attr_value.relation_name)

                relations.append(attr_value)

        attrs["__relations__"] = relations

        return super().__new__(cls, name, bases, attrs)

    @property
    def namespace(cls) -> str:
        return cls.__namespace__


class ArrakisNamespace(object, metaclass=_ArrakisNamespaceMeta):
    """Declarative namespace config class for representing an entire authorization service
    namespace. Any fields defined under this class of type Relation will be made available
    as ObjectAndRelation constructors for communicating with the client API.
    """

    __relations__: List[Relation] = []
    __namespace__: str = ""

    def __init__(self, arrakis_object_id: str):
        self._arrakis_object_id = arrakis_object_id
        self._onrs = {}

        for relation in self.__relations__:
            assert isinstance(relation, Relation)
            onr = ObjectAndRelation(self, relation.relation_name)
            setattr(self, relation._attr_key, onr)
            self._onrs[relation.relation_name] = onr

    def relation(self, relation_name: str) -> ObjectAndRelation:
        return self._onrs[relation_name]

    def __repr__(self) -> str:
        return f"{self.__namespace__}:{self._arrakis_object_id}"

    @property
    def namespace(self) -> str:
        return self.__namespace__

    @property
    def object_id(self) -> str:
        return self._arrakis_object_id

    def __eq__(self, other: "ArrakisNamespace") -> bool:
        return (
            self._arrakis_object_id == other._arrakis_object_id
            and self.__namespace__ == other.__namespace__
        )
