"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ReadSchemaRequest(google.protobuf.message.Message):
    """ReadSchemaRequest returns the schema from the database."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ReadSchemaRequest = ReadSchemaRequest

class ReadSchemaResponse(google.protobuf.message.Message):
    """ReadSchemaResponse is the resulting data after having read the Object
    Definitions from a Schema.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCHEMA_TEXT_FIELD_NUMBER: builtins.int
    schema_text: builtins.str
    """schema_text is the textual form of the current schema in the system"""
    def __init__(
        self,
        *,
        schema_text: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["schema_text", b"schema_text"]) -> None: ...

global___ReadSchemaResponse = ReadSchemaResponse

class WriteSchemaRequest(google.protobuf.message.Message):
    """WriteSchemaRequest is the required data used to "upsert" the Schema of a
    Permissions System.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCHEMA_FIELD_NUMBER: builtins.int
    schema: builtins.str
    """The Schema containing one or more Object Definitions that will be written
    to the Permissions System.
    256KiB
    """
    def __init__(
        self,
        *,
        schema: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["schema", b"schema"]) -> None: ...

global___WriteSchemaRequest = WriteSchemaRequest

class WriteSchemaResponse(google.protobuf.message.Message):
    """WriteSchemaResponse is the resulting data after having written a Schema to
    a Permissions System.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___WriteSchemaResponse = WriteSchemaResponse
