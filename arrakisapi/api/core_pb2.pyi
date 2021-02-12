# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class RelationTuple(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def object_and_relation(self) -> type___ObjectAndRelation: ...

    @property
    def user(self) -> type___User: ...

    def __init__(self,
        *,
        object_and_relation : typing___Optional[type___ObjectAndRelation] = None,
        user : typing___Optional[type___User] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"object_and_relation",b"object_and_relation",u"user",b"user"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"object_and_relation",b"object_and_relation",u"user",b"user"]) -> None: ...
type___RelationTuple = RelationTuple

class ObjectAndRelation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    object_id: typing___Text = ...
    relation: typing___Text = ...

    def __init__(self,
        *,
        namespace : typing___Optional[typing___Text] = None,
        object_id : typing___Optional[typing___Text] = None,
        relation : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"namespace",b"namespace",u"object_id",b"object_id",u"relation",b"relation"]) -> None: ...
type___ObjectAndRelation = ObjectAndRelation

class User(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def userset(self) -> type___ObjectAndRelation: ...

    def __init__(self,
        *,
        userset : typing___Optional[type___ObjectAndRelation] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"user_oneof",b"user_oneof",u"userset",b"userset"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"user_oneof",b"user_oneof",u"userset",b"userset"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"user_oneof",b"user_oneof"]) -> typing_extensions___Literal["userset"]: ...
type___User = User

class Zookie(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    token: typing___Text = ...

    def __init__(self,
        *,
        token : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"token",b"token"]) -> None: ...
type___Zookie = Zookie

class RelationTupleUpdate(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    OperationValue = typing___NewType('OperationValue', builtin___int)
    type___OperationValue = OperationValue
    Operation: _Operation
    class _Operation(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[RelationTupleUpdate.OperationValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNKNOWN = typing___cast(RelationTupleUpdate.OperationValue, 0)
        CREATE = typing___cast(RelationTupleUpdate.OperationValue, 1)
        TOUCH = typing___cast(RelationTupleUpdate.OperationValue, 2)
        DELETE = typing___cast(RelationTupleUpdate.OperationValue, 3)
    UNKNOWN = typing___cast(RelationTupleUpdate.OperationValue, 0)
    CREATE = typing___cast(RelationTupleUpdate.OperationValue, 1)
    TOUCH = typing___cast(RelationTupleUpdate.OperationValue, 2)
    DELETE = typing___cast(RelationTupleUpdate.OperationValue, 3)
    type___Operation = Operation

    operation: type___RelationTupleUpdate.OperationValue = ...

    @property
    def tuple(self) -> type___RelationTuple: ...

    def __init__(self,
        *,
        operation : typing___Optional[type___RelationTupleUpdate.OperationValue] = None,
        tuple : typing___Optional[type___RelationTuple] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"tuple",b"tuple"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"operation",b"operation",u"tuple",b"tuple"]) -> None: ...
type___RelationTupleUpdate = RelationTupleUpdate

class RelationTupleTreeNode(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def intermediate_node(self) -> type___SetOperationUserset: ...

    @property
    def leaf_node(self) -> type___DirectUserset: ...

    @property
    def expanded(self) -> type___ObjectAndRelation: ...

    def __init__(self,
        *,
        intermediate_node : typing___Optional[type___SetOperationUserset] = None,
        leaf_node : typing___Optional[type___DirectUserset] = None,
        expanded : typing___Optional[type___ObjectAndRelation] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"expanded",b"expanded",u"intermediate_node",b"intermediate_node",u"leaf_node",b"leaf_node",u"node_type",b"node_type"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"expanded",b"expanded",u"intermediate_node",b"intermediate_node",u"leaf_node",b"leaf_node",u"node_type",b"node_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"node_type",b"node_type"]) -> typing_extensions___Literal["intermediate_node","leaf_node"]: ...
type___RelationTupleTreeNode = RelationTupleTreeNode

class SetOperationUserset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    OperationValue = typing___NewType('OperationValue', builtin___int)
    type___OperationValue = OperationValue
    Operation: _Operation
    class _Operation(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SetOperationUserset.OperationValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        INVALID = typing___cast(SetOperationUserset.OperationValue, 0)
        UNION = typing___cast(SetOperationUserset.OperationValue, 1)
        INTERSECTION = typing___cast(SetOperationUserset.OperationValue, 2)
        EXCLUSION = typing___cast(SetOperationUserset.OperationValue, 3)
    INVALID = typing___cast(SetOperationUserset.OperationValue, 0)
    UNION = typing___cast(SetOperationUserset.OperationValue, 1)
    INTERSECTION = typing___cast(SetOperationUserset.OperationValue, 2)
    EXCLUSION = typing___cast(SetOperationUserset.OperationValue, 3)
    type___Operation = Operation

    operation: type___SetOperationUserset.OperationValue = ...

    @property
    def child_nodes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___RelationTupleTreeNode]: ...

    def __init__(self,
        *,
        operation : typing___Optional[type___SetOperationUserset.OperationValue] = None,
        child_nodes : typing___Optional[typing___Iterable[type___RelationTupleTreeNode]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"child_nodes",b"child_nodes",u"operation",b"operation"]) -> None: ...
type___SetOperationUserset = SetOperationUserset

class DirectUserset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def users(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___User]: ...

    def __init__(self,
        *,
        users : typing___Optional[typing___Iterable[type___User]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"users",b"users"]) -> None: ...
type___DirectUserset = DirectUserset
