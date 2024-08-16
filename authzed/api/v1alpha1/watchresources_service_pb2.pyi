from google.api import annotations_pb2 as _annotations_pb2
from validate import validate_pb2 as _validate_pb2
from authzed.api.v1 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchResourcesRequest(_message.Message):
    __slots__ = ("resource_object_type", "permission", "subject_object_type", "optional_subject_relation", "optional_start_cursor")
    RESOURCE_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SUBJECT_RELATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_START_CURSOR_FIELD_NUMBER: _ClassVar[int]
    resource_object_type: str
    permission: str
    subject_object_type: str
    optional_subject_relation: str
    optional_start_cursor: _core_pb2.ZedToken
    def __init__(self, resource_object_type: _Optional[str] = ..., permission: _Optional[str] = ..., subject_object_type: _Optional[str] = ..., optional_subject_relation: _Optional[str] = ..., optional_start_cursor: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class PermissionUpdate(_message.Message):
    __slots__ = ("subject", "resource", "relation", "updated_permission")
    class Permissionship(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERMISSIONSHIP_UNSPECIFIED: _ClassVar[PermissionUpdate.Permissionship]
        PERMISSIONSHIP_NO_PERMISSION: _ClassVar[PermissionUpdate.Permissionship]
        PERMISSIONSHIP_HAS_PERMISSION: _ClassVar[PermissionUpdate.Permissionship]
    PERMISSIONSHIP_UNSPECIFIED: PermissionUpdate.Permissionship
    PERMISSIONSHIP_NO_PERMISSION: PermissionUpdate.Permissionship
    PERMISSIONSHIP_HAS_PERMISSION: PermissionUpdate.Permissionship
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    subject: _core_pb2.SubjectReference
    resource: _core_pb2.ObjectReference
    relation: str
    updated_permission: PermissionUpdate.Permissionship
    def __init__(self, subject: _Optional[_Union[_core_pb2.SubjectReference, _Mapping]] = ..., resource: _Optional[_Union[_core_pb2.ObjectReference, _Mapping]] = ..., relation: _Optional[str] = ..., updated_permission: _Optional[_Union[PermissionUpdate.Permissionship, str]] = ...) -> None: ...

class WatchResourcesResponse(_message.Message):
    __slots__ = ("updates", "changes_through")
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    CHANGES_THROUGH_FIELD_NUMBER: _ClassVar[int]
    updates: _containers.RepeatedCompositeFieldContainer[PermissionUpdate]
    changes_through: _core_pb2.ZedToken
    def __init__(self, updates: _Optional[_Iterable[_Union[PermissionUpdate, _Mapping]]] = ..., changes_through: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...
