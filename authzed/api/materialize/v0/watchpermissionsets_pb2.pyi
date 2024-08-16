from authzed.api.v1 import core_pb2 as _core_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchPermissionSetsRequest(_message.Message):
    __slots__ = ("optional_starting_after",)
    OPTIONAL_STARTING_AFTER_FIELD_NUMBER: _ClassVar[int]
    optional_starting_after: _core_pb2.ZedToken
    def __init__(self, optional_starting_after: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class WatchPermissionSetsResponse(_message.Message):
    __slots__ = ("change", "completed_revision", "lookup_permission_sets_required")
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_REVISION_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_PERMISSION_SETS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    change: PermissionSetChange
    completed_revision: _core_pb2.ZedToken
    lookup_permission_sets_required: LookupPermissionSetsRequired
    def __init__(self, change: _Optional[_Union[PermissionSetChange, _Mapping]] = ..., completed_revision: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., lookup_permission_sets_required: _Optional[_Union[LookupPermissionSetsRequired, _Mapping]] = ...) -> None: ...

class Cursor(_message.Message):
    __slots__ = ("limit", "token", "starting_index", "completed_members")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    STARTING_INDEX_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    limit: int
    token: _core_pb2.ZedToken
    starting_index: int
    completed_members: bool
    def __init__(self, limit: _Optional[int] = ..., token: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., starting_index: _Optional[int] = ..., completed_members: bool = ...) -> None: ...

class LookupPermissionSetsRequest(_message.Message):
    __slots__ = ("limit", "optional_starting_after_cursor")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STARTING_AFTER_CURSOR_FIELD_NUMBER: _ClassVar[int]
    limit: int
    optional_starting_after_cursor: Cursor
    def __init__(self, limit: _Optional[int] = ..., optional_starting_after_cursor: _Optional[_Union[Cursor, _Mapping]] = ...) -> None: ...

class LookupPermissionSetsResponse(_message.Message):
    __slots__ = ("change", "cursor")
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    change: PermissionSetChange
    cursor: Cursor
    def __init__(self, change: _Optional[_Union[PermissionSetChange, _Mapping]] = ..., cursor: _Optional[_Union[Cursor, _Mapping]] = ...) -> None: ...

class PermissionSetChange(_message.Message):
    __slots__ = ("at_revision", "operation", "parent_set", "child_set", "child_member")
    class SetOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SET_OPERATION_UNSPECIFIED: _ClassVar[PermissionSetChange.SetOperation]
        SET_OPERATION_ADDED: _ClassVar[PermissionSetChange.SetOperation]
        SET_OPERATION_REMOVED: _ClassVar[PermissionSetChange.SetOperation]
    SET_OPERATION_UNSPECIFIED: PermissionSetChange.SetOperation
    SET_OPERATION_ADDED: PermissionSetChange.SetOperation
    SET_OPERATION_REMOVED: PermissionSetChange.SetOperation
    AT_REVISION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PARENT_SET_FIELD_NUMBER: _ClassVar[int]
    CHILD_SET_FIELD_NUMBER: _ClassVar[int]
    CHILD_MEMBER_FIELD_NUMBER: _ClassVar[int]
    at_revision: _core_pb2.ZedToken
    operation: PermissionSetChange.SetOperation
    parent_set: SetReference
    child_set: SetReference
    child_member: MemberReference
    def __init__(self, at_revision: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., operation: _Optional[_Union[PermissionSetChange.SetOperation, str]] = ..., parent_set: _Optional[_Union[SetReference, _Mapping]] = ..., child_set: _Optional[_Union[SetReference, _Mapping]] = ..., child_member: _Optional[_Union[MemberReference, _Mapping]] = ...) -> None: ...

class SetReference(_message.Message):
    __slots__ = ("object_type", "object_id", "permission_or_relation")
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_OR_RELATION_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    permission_or_relation: str
    def __init__(self, object_type: _Optional[str] = ..., object_id: _Optional[str] = ..., permission_or_relation: _Optional[str] = ...) -> None: ...

class MemberReference(_message.Message):
    __slots__ = ("object_type", "object_id", "optional_permission_or_relation")
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PERMISSION_OR_RELATION_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    optional_permission_or_relation: str
    def __init__(self, object_type: _Optional[str] = ..., object_id: _Optional[str] = ..., optional_permission_or_relation: _Optional[str] = ...) -> None: ...

class LookupPermissionSetsRequired(_message.Message):
    __slots__ = ("required_lookup_at",)
    REQUIRED_LOOKUP_AT_FIELD_NUMBER: _ClassVar[int]
    required_lookup_at: _core_pb2.ZedToken
    def __init__(self, required_lookup_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...
