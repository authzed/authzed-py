"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import authzed.api.v0.core_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class FormatSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SCHEMA_FIELD_NUMBER: builtins.int
    schema: typing.Text
    def __init__(self,
        *,
        schema: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["schema",b"schema"]) -> None: ...
global___FormatSchemaRequest = FormatSchemaRequest

class FormatSchemaResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERROR_FIELD_NUMBER: builtins.int
    FORMATTED_SCHEMA_FIELD_NUMBER: builtins.int
    @property
    def error(self) -> global___DeveloperError: ...
    formatted_schema: typing.Text
    def __init__(self,
        *,
        error: typing.Optional[global___DeveloperError] = ...,
        formatted_schema: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","formatted_schema",b"formatted_schema"]) -> None: ...
global___FormatSchemaResponse = FormatSchemaResponse

class UpgradeSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAMESPACE_CONFIGS_FIELD_NUMBER: builtins.int
    @property
    def namespace_configs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        namespace_configs: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["namespace_configs",b"namespace_configs"]) -> None: ...
global___UpgradeSchemaRequest = UpgradeSchemaRequest

class UpgradeSchemaResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERROR_FIELD_NUMBER: builtins.int
    UPGRADED_SCHEMA_FIELD_NUMBER: builtins.int
    @property
    def error(self) -> global___DeveloperError: ...
    upgraded_schema: typing.Text
    def __init__(self,
        *,
        error: typing.Optional[global___DeveloperError] = ...,
        upgraded_schema: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","upgraded_schema",b"upgraded_schema"]) -> None: ...
global___UpgradeSchemaResponse = UpgradeSchemaResponse

class ShareRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SCHEMA_FIELD_NUMBER: builtins.int
    RELATIONSHIPS_YAML_FIELD_NUMBER: builtins.int
    VALIDATION_YAML_FIELD_NUMBER: builtins.int
    ASSERTIONS_YAML_FIELD_NUMBER: builtins.int
    schema: typing.Text
    relationships_yaml: typing.Text
    validation_yaml: typing.Text
    assertions_yaml: typing.Text
    def __init__(self,
        *,
        schema: typing.Text = ...,
        relationships_yaml: typing.Text = ...,
        validation_yaml: typing.Text = ...,
        assertions_yaml: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assertions_yaml",b"assertions_yaml","relationships_yaml",b"relationships_yaml","schema",b"schema","validation_yaml",b"validation_yaml"]) -> None: ...
global___ShareRequest = ShareRequest

class ShareResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SHARE_REFERENCE_FIELD_NUMBER: builtins.int
    share_reference: typing.Text
    def __init__(self,
        *,
        share_reference: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["share_reference",b"share_reference"]) -> None: ...
global___ShareResponse = ShareResponse

class LookupShareRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SHARE_REFERENCE_FIELD_NUMBER: builtins.int
    share_reference: typing.Text
    def __init__(self,
        *,
        share_reference: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["share_reference",b"share_reference"]) -> None: ...
global___LookupShareRequest = LookupShareRequest

class LookupShareResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _LookupStatus:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _LookupStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LookupShareResponse._LookupStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN_REFERENCE: LookupShareResponse._LookupStatus.ValueType  # 0
        FAILED_TO_LOOKUP: LookupShareResponse._LookupStatus.ValueType  # 1
        VALID_REFERENCE: LookupShareResponse._LookupStatus.ValueType  # 2
        UPGRADED_REFERENCE: LookupShareResponse._LookupStatus.ValueType  # 3
    class LookupStatus(_LookupStatus, metaclass=_LookupStatusEnumTypeWrapper):
        pass

    UNKNOWN_REFERENCE: LookupShareResponse.LookupStatus.ValueType  # 0
    FAILED_TO_LOOKUP: LookupShareResponse.LookupStatus.ValueType  # 1
    VALID_REFERENCE: LookupShareResponse.LookupStatus.ValueType  # 2
    UPGRADED_REFERENCE: LookupShareResponse.LookupStatus.ValueType  # 3

    STATUS_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    RELATIONSHIPS_YAML_FIELD_NUMBER: builtins.int
    VALIDATION_YAML_FIELD_NUMBER: builtins.int
    ASSERTIONS_YAML_FIELD_NUMBER: builtins.int
    status: global___LookupShareResponse.LookupStatus.ValueType
    schema: typing.Text
    relationships_yaml: typing.Text
    validation_yaml: typing.Text
    assertions_yaml: typing.Text
    def __init__(self,
        *,
        status: global___LookupShareResponse.LookupStatus.ValueType = ...,
        schema: typing.Text = ...,
        relationships_yaml: typing.Text = ...,
        validation_yaml: typing.Text = ...,
        assertions_yaml: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assertions_yaml",b"assertions_yaml","relationships_yaml",b"relationships_yaml","schema",b"schema","status",b"status","validation_yaml",b"validation_yaml"]) -> None: ...
global___LookupShareResponse = LookupShareResponse

class RequestContext(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SCHEMA_FIELD_NUMBER: builtins.int
    RELATIONSHIPS_FIELD_NUMBER: builtins.int
    schema: typing.Text
    @property
    def relationships(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v0.core_pb2.RelationTuple]: ...
    def __init__(self,
        *,
        schema: typing.Text = ...,
        relationships: typing.Optional[typing.Iterable[authzed.api.v0.core_pb2.RelationTuple]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["relationships",b"relationships","schema",b"schema"]) -> None: ...
global___RequestContext = RequestContext

class EditCheckRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTEXT_FIELD_NUMBER: builtins.int
    CHECK_RELATIONSHIPS_FIELD_NUMBER: builtins.int
    @property
    def context(self) -> global___RequestContext: ...
    @property
    def check_relationships(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v0.core_pb2.RelationTuple]: ...
    def __init__(self,
        *,
        context: typing.Optional[global___RequestContext] = ...,
        check_relationships: typing.Optional[typing.Iterable[authzed.api.v0.core_pb2.RelationTuple]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["context",b"context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["check_relationships",b"check_relationships","context",b"context"]) -> None: ...
global___EditCheckRequest = EditCheckRequest

class EditCheckResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RELATIONSHIP_FIELD_NUMBER: builtins.int
    IS_MEMBER_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def relationship(self) -> authzed.api.v0.core_pb2.RelationTuple: ...
    is_member: builtins.bool
    @property
    def error(self) -> global___DeveloperError: ...
    def __init__(self,
        *,
        relationship: typing.Optional[authzed.api.v0.core_pb2.RelationTuple] = ...,
        is_member: builtins.bool = ...,
        error: typing.Optional[global___DeveloperError] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","relationship",b"relationship"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","is_member",b"is_member","relationship",b"relationship"]) -> None: ...
global___EditCheckResult = EditCheckResult

class EditCheckResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REQUEST_ERRORS_FIELD_NUMBER: builtins.int
    CHECK_RESULTS_FIELD_NUMBER: builtins.int
    @property
    def request_errors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeveloperError]: ...
    @property
    def check_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EditCheckResult]: ...
    def __init__(self,
        *,
        request_errors: typing.Optional[typing.Iterable[global___DeveloperError]] = ...,
        check_results: typing.Optional[typing.Iterable[global___EditCheckResult]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["check_results",b"check_results","request_errors",b"request_errors"]) -> None: ...
global___EditCheckResponse = EditCheckResponse

class ValidateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTEXT_FIELD_NUMBER: builtins.int
    VALIDATION_YAML_FIELD_NUMBER: builtins.int
    UPDATE_VALIDATION_YAML_FIELD_NUMBER: builtins.int
    ASSERTIONS_YAML_FIELD_NUMBER: builtins.int
    @property
    def context(self) -> global___RequestContext: ...
    validation_yaml: typing.Text
    update_validation_yaml: builtins.bool
    assertions_yaml: typing.Text
    def __init__(self,
        *,
        context: typing.Optional[global___RequestContext] = ...,
        validation_yaml: typing.Text = ...,
        update_validation_yaml: builtins.bool = ...,
        assertions_yaml: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["context",b"context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assertions_yaml",b"assertions_yaml","context",b"context","update_validation_yaml",b"update_validation_yaml","validation_yaml",b"validation_yaml"]) -> None: ...
global___ValidateRequest = ValidateRequest

class ValidateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REQUEST_ERRORS_FIELD_NUMBER: builtins.int
    VALIDATION_ERRORS_FIELD_NUMBER: builtins.int
    UPDATED_VALIDATION_YAML_FIELD_NUMBER: builtins.int
    @property
    def request_errors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeveloperError]: ...
    @property
    def validation_errors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeveloperError]: ...
    updated_validation_yaml: typing.Text
    def __init__(self,
        *,
        request_errors: typing.Optional[typing.Iterable[global___DeveloperError]] = ...,
        validation_errors: typing.Optional[typing.Iterable[global___DeveloperError]] = ...,
        updated_validation_yaml: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["request_errors",b"request_errors","updated_validation_yaml",b"updated_validation_yaml","validation_errors",b"validation_errors"]) -> None: ...
global___ValidateResponse = ValidateResponse

class DeveloperError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class _Source:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _SourceEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeveloperError._Source.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN_SOURCE: DeveloperError._Source.ValueType  # 0
        SCHEMA: DeveloperError._Source.ValueType  # 1
        RELATIONSHIP: DeveloperError._Source.ValueType  # 2
        VALIDATION_YAML: DeveloperError._Source.ValueType  # 3
        CHECK_WATCH: DeveloperError._Source.ValueType  # 4
        ASSERTION: DeveloperError._Source.ValueType  # 5
    class Source(_Source, metaclass=_SourceEnumTypeWrapper):
        pass

    UNKNOWN_SOURCE: DeveloperError.Source.ValueType  # 0
    SCHEMA: DeveloperError.Source.ValueType  # 1
    RELATIONSHIP: DeveloperError.Source.ValueType  # 2
    VALIDATION_YAML: DeveloperError.Source.ValueType  # 3
    CHECK_WATCH: DeveloperError.Source.ValueType  # 4
    ASSERTION: DeveloperError.Source.ValueType  # 5

    class _ErrorKind:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ErrorKindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeveloperError._ErrorKind.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN_KIND: DeveloperError._ErrorKind.ValueType  # 0
        PARSE_ERROR: DeveloperError._ErrorKind.ValueType  # 1
        SCHEMA_ISSUE: DeveloperError._ErrorKind.ValueType  # 2
        DUPLICATE_RELATIONSHIP: DeveloperError._ErrorKind.ValueType  # 3
        MISSING_EXPECTED_RELATIONSHIP: DeveloperError._ErrorKind.ValueType  # 4
        EXTRA_RELATIONSHIP_FOUND: DeveloperError._ErrorKind.ValueType  # 5
        UNKNOWN_OBJECT_TYPE: DeveloperError._ErrorKind.ValueType  # 6
        UNKNOWN_RELATION: DeveloperError._ErrorKind.ValueType  # 7
        MAXIMUM_RECURSION: DeveloperError._ErrorKind.ValueType  # 8
        ASSERTION_FAILED: DeveloperError._ErrorKind.ValueType  # 9
    class ErrorKind(_ErrorKind, metaclass=_ErrorKindEnumTypeWrapper):
        pass

    UNKNOWN_KIND: DeveloperError.ErrorKind.ValueType  # 0
    PARSE_ERROR: DeveloperError.ErrorKind.ValueType  # 1
    SCHEMA_ISSUE: DeveloperError.ErrorKind.ValueType  # 2
    DUPLICATE_RELATIONSHIP: DeveloperError.ErrorKind.ValueType  # 3
    MISSING_EXPECTED_RELATIONSHIP: DeveloperError.ErrorKind.ValueType  # 4
    EXTRA_RELATIONSHIP_FOUND: DeveloperError.ErrorKind.ValueType  # 5
    UNKNOWN_OBJECT_TYPE: DeveloperError.ErrorKind.ValueType  # 6
    UNKNOWN_RELATION: DeveloperError.ErrorKind.ValueType  # 7
    MAXIMUM_RECURSION: DeveloperError.ErrorKind.ValueType  # 8
    ASSERTION_FAILED: DeveloperError.ErrorKind.ValueType  # 9

    MESSAGE_FIELD_NUMBER: builtins.int
    LINE_FIELD_NUMBER: builtins.int
    COLUMN_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    message: typing.Text
    line: builtins.int
    column: builtins.int
    source: global___DeveloperError.Source.ValueType
    kind: global___DeveloperError.ErrorKind.ValueType
    @property
    def path(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    context: typing.Text
    """context holds the context for the error. For schema issues, this will be the
    name of the object type. For relationship issues, the full relationship string.
    """

    def __init__(self,
        *,
        message: typing.Text = ...,
        line: builtins.int = ...,
        column: builtins.int = ...,
        source: global___DeveloperError.Source.ValueType = ...,
        kind: global___DeveloperError.ErrorKind.ValueType = ...,
        path: typing.Optional[typing.Iterable[typing.Text]] = ...,
        context: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["column",b"column","context",b"context","kind",b"kind","line",b"line","message",b"message","path",b"path","source",b"source"]) -> None: ...
global___DeveloperError = DeveloperError
