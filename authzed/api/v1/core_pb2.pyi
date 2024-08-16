from google.protobuf import struct_pb2 as _struct_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Relationship(_message.Message):
    __slots__ = ("resource", "relation", "subject", "optional_caveat")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CAVEAT_FIELD_NUMBER: _ClassVar[int]
    resource: ObjectReference
    relation: str
    subject: SubjectReference
    optional_caveat: ContextualizedCaveat
    def __init__(self, resource: _Optional[_Union[ObjectReference, _Mapping]] = ..., relation: _Optional[str] = ..., subject: _Optional[_Union[SubjectReference, _Mapping]] = ..., optional_caveat: _Optional[_Union[ContextualizedCaveat, _Mapping]] = ...) -> None: ...

class ContextualizedCaveat(_message.Message):
    __slots__ = ("caveat_name", "context")
    CAVEAT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    caveat_name: str
    context: _struct_pb2.Struct
    def __init__(self, caveat_name: _Optional[str] = ..., context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class SubjectReference(_message.Message):
    __slots__ = ("object", "optional_relation")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_RELATION_FIELD_NUMBER: _ClassVar[int]
    object: ObjectReference
    optional_relation: str
    def __init__(self, object: _Optional[_Union[ObjectReference, _Mapping]] = ..., optional_relation: _Optional[str] = ...) -> None: ...

class ObjectReference(_message.Message):
    __slots__ = ("object_type", "object_id")
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    def __init__(self, object_type: _Optional[str] = ..., object_id: _Optional[str] = ...) -> None: ...

class ZedToken(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class Cursor(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class RelationshipUpdate(_message.Message):
    __slots__ = ("operation", "relationship")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_UNSPECIFIED: _ClassVar[RelationshipUpdate.Operation]
        OPERATION_CREATE: _ClassVar[RelationshipUpdate.Operation]
        OPERATION_TOUCH: _ClassVar[RelationshipUpdate.Operation]
        OPERATION_DELETE: _ClassVar[RelationshipUpdate.Operation]
    OPERATION_UNSPECIFIED: RelationshipUpdate.Operation
    OPERATION_CREATE: RelationshipUpdate.Operation
    OPERATION_TOUCH: RelationshipUpdate.Operation
    OPERATION_DELETE: RelationshipUpdate.Operation
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    operation: RelationshipUpdate.Operation
    relationship: Relationship
    def __init__(self, operation: _Optional[_Union[RelationshipUpdate.Operation, str]] = ..., relationship: _Optional[_Union[Relationship, _Mapping]] = ...) -> None: ...

class PermissionRelationshipTree(_message.Message):
    __slots__ = ("intermediate", "leaf", "expanded_object", "expanded_relation")
    INTERMEDIATE_FIELD_NUMBER: _ClassVar[int]
    LEAF_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_OBJECT_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_RELATION_FIELD_NUMBER: _ClassVar[int]
    intermediate: AlgebraicSubjectSet
    leaf: DirectSubjectSet
    expanded_object: ObjectReference
    expanded_relation: str
    def __init__(self, intermediate: _Optional[_Union[AlgebraicSubjectSet, _Mapping]] = ..., leaf: _Optional[_Union[DirectSubjectSet, _Mapping]] = ..., expanded_object: _Optional[_Union[ObjectReference, _Mapping]] = ..., expanded_relation: _Optional[str] = ...) -> None: ...

class AlgebraicSubjectSet(_message.Message):
    __slots__ = ("operation", "children")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_UNSPECIFIED: _ClassVar[AlgebraicSubjectSet.Operation]
        OPERATION_UNION: _ClassVar[AlgebraicSubjectSet.Operation]
        OPERATION_INTERSECTION: _ClassVar[AlgebraicSubjectSet.Operation]
        OPERATION_EXCLUSION: _ClassVar[AlgebraicSubjectSet.Operation]
    OPERATION_UNSPECIFIED: AlgebraicSubjectSet.Operation
    OPERATION_UNION: AlgebraicSubjectSet.Operation
    OPERATION_INTERSECTION: AlgebraicSubjectSet.Operation
    OPERATION_EXCLUSION: AlgebraicSubjectSet.Operation
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    operation: AlgebraicSubjectSet.Operation
    children: _containers.RepeatedCompositeFieldContainer[PermissionRelationshipTree]
    def __init__(self, operation: _Optional[_Union[AlgebraicSubjectSet.Operation, str]] = ..., children: _Optional[_Iterable[_Union[PermissionRelationshipTree, _Mapping]]] = ...) -> None: ...

class DirectSubjectSet(_message.Message):
    __slots__ = ("subjects",)
    SUBJECTS_FIELD_NUMBER: _ClassVar[int]
    subjects: _containers.RepeatedCompositeFieldContainer[SubjectReference]
    def __init__(self, subjects: _Optional[_Iterable[_Union[SubjectReference, _Mapping]]] = ...) -> None: ...

class PartialCaveatInfo(_message.Message):
    __slots__ = ("missing_required_context",)
    MISSING_REQUIRED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    missing_required_context: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, missing_required_context: _Optional[_Iterable[str]] = ...) -> None: ...
