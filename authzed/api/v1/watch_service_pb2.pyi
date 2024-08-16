from google.api import annotations_pb2 as _annotations_pb2
from validate import validate_pb2 as _validate_pb2
from authzed.api.v1 import core_pb2 as _core_pb2
from authzed.api.v1 import permission_service_pb2 as _permission_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchRequest(_message.Message):
    __slots__ = ("optional_object_types", "optional_start_cursor", "optional_relationship_filters")
    OPTIONAL_OBJECT_TYPES_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_START_CURSOR_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_RELATIONSHIP_FILTERS_FIELD_NUMBER: _ClassVar[int]
    optional_object_types: _containers.RepeatedScalarFieldContainer[str]
    optional_start_cursor: _core_pb2.ZedToken
    optional_relationship_filters: _containers.RepeatedCompositeFieldContainer[_permission_service_pb2.RelationshipFilter]
    def __init__(self, optional_object_types: _Optional[_Iterable[str]] = ..., optional_start_cursor: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., optional_relationship_filters: _Optional[_Iterable[_Union[_permission_service_pb2.RelationshipFilter, _Mapping]]] = ...) -> None: ...

class WatchResponse(_message.Message):
    __slots__ = ("updates", "changes_through")
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    CHANGES_THROUGH_FIELD_NUMBER: _ClassVar[int]
    updates: _containers.RepeatedCompositeFieldContainer[_core_pb2.RelationshipUpdate]
    changes_through: _core_pb2.ZedToken
    def __init__(self, updates: _Optional[_Iterable[_Union[_core_pb2.RelationshipUpdate, _Mapping]]] = ..., changes_through: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...
