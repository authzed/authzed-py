from validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RelationTuple(_message.Message):
    __slots__ = ("object_and_relation", "user")
    OBJECT_AND_RELATION_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    object_and_relation: ObjectAndRelation
    user: User
    def __init__(self, object_and_relation: _Optional[_Union[ObjectAndRelation, _Mapping]] = ..., user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class ObjectAndRelation(_message.Message):
    __slots__ = ("namespace", "object_id", "relation")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    object_id: str
    relation: str
    def __init__(self, namespace: _Optional[str] = ..., object_id: _Optional[str] = ..., relation: _Optional[str] = ...) -> None: ...

class RelationReference(_message.Message):
    __slots__ = ("namespace", "relation")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    relation: str
    def __init__(self, namespace: _Optional[str] = ..., relation: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("userset",)
    USERSET_FIELD_NUMBER: _ClassVar[int]
    userset: ObjectAndRelation
    def __init__(self, userset: _Optional[_Union[ObjectAndRelation, _Mapping]] = ...) -> None: ...
