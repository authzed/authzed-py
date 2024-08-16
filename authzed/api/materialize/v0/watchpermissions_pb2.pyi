from authzed.api.v1 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchPermissionsRequest(_message.Message):
    __slots__ = ("permissions", "optional_starting_after")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STARTING_AFTER_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[WatchedPermission]
    optional_starting_after: _core_pb2.ZedToken
    def __init__(self, permissions: _Optional[_Iterable[_Union[WatchedPermission, _Mapping]]] = ..., optional_starting_after: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class WatchedPermission(_message.Message):
    __slots__ = ("resource_type", "permission", "subject_type", "optional_subject_relation")
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SUBJECT_RELATION_FIELD_NUMBER: _ClassVar[int]
    resource_type: str
    permission: str
    subject_type: str
    optional_subject_relation: str
    def __init__(self, resource_type: _Optional[str] = ..., permission: _Optional[str] = ..., subject_type: _Optional[str] = ..., optional_subject_relation: _Optional[str] = ...) -> None: ...

class WatchPermissionsResponse(_message.Message):
    __slots__ = ("change", "completed_revision")
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_REVISION_FIELD_NUMBER: _ClassVar[int]
    change: PermissionChange
    completed_revision: _core_pb2.ZedToken
    def __init__(self, change: _Optional[_Union[PermissionChange, _Mapping]] = ..., completed_revision: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class PermissionChange(_message.Message):
    __slots__ = ("revision", "resource", "permission", "subject", "permissionship")
    class Permissionship(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERMISSIONSHIP_UNSPECIFIED: _ClassVar[PermissionChange.Permissionship]
        PERMISSIONSHIP_NO_PERMISSION: _ClassVar[PermissionChange.Permissionship]
        PERMISSIONSHIP_HAS_PERMISSION: _ClassVar[PermissionChange.Permissionship]
        PERMISSIONSHIP_CONDITIONAL_PERMISSION: _ClassVar[PermissionChange.Permissionship]
    PERMISSIONSHIP_UNSPECIFIED: PermissionChange.Permissionship
    PERMISSIONSHIP_NO_PERMISSION: PermissionChange.Permissionship
    PERMISSIONSHIP_HAS_PERMISSION: PermissionChange.Permissionship
    PERMISSIONSHIP_CONDITIONAL_PERMISSION: PermissionChange.Permissionship
    REVISION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONSHIP_FIELD_NUMBER: _ClassVar[int]
    revision: _core_pb2.ZedToken
    resource: _core_pb2.ObjectReference
    permission: str
    subject: _core_pb2.SubjectReference
    permissionship: PermissionChange.Permissionship
    def __init__(self, revision: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., resource: _Optional[_Union[_core_pb2.ObjectReference, _Mapping]] = ..., permission: _Optional[str] = ..., subject: _Optional[_Union[_core_pb2.SubjectReference, _Mapping]] = ..., permissionship: _Optional[_Union[PermissionChange.Permissionship, str]] = ...) -> None: ...
