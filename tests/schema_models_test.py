import subprocess
import sys

from authzed.api.v1 import schema_service_pb2

# Exercise the public import path used by consumers, rather than importing the
# generated module directly. The same program must work at runtime and in mypy.
CONSUMER = """
from typing_extensions import assert_type
from authzed.api.v1 import (
    ComputablePermissionsRequest,
    ComputablePermissionsResponse,
    DependentRelationsRequest,
    DependentRelationsResponse,
    DiffSchemaRequest,
    DiffSchemaResponse,
    ReflectSchemaRequest,
    ReflectSchemaResponse,
    ReflectionCaveat,
    ReflectionCaveatParameter,
    ReflectionCaveatParameterTypeChange,
    ReflectionDefinition,
    ReflectionPermission,
    ReflectionRelation,
    ReflectionRelationReference,
    ReflectionRelationSubjectTypeChange,
    ReflectionSchemaDiff,
    ReflectionSchemaFilter,
    ReflectionTypeReference,
)

request = ReflectSchemaRequest(
    optional_filters=[ReflectionSchemaFilter(optional_definition_name_filter="document")]
)
assert_type(request, ReflectSchemaRequest)
assert_type(request.SerializeToString(), bytes)

response = ReflectSchemaResponse(
    definitions=[ReflectionDefinition(name="document")]
)
assert_type(response.definitions[0], ReflectionDefinition)
assert_type(response.definitions[0].name, str)
"""


def test_public_schema_models_at_runtime():
    namespace = {}
    exec(CONSUMER, namespace)
    request = namespace["request"]
    decoded = schema_service_pb2.ReflectSchemaRequest.FromString(request.SerializeToString())
    assert decoded.optional_filters[0].optional_definition_name_filter == "document"
    assert namespace["response"].definitions[0].name == "document"


def test_public_schema_models_typecheck(tmp_path):
    consumer = tmp_path / "schema_consumer.py"
    consumer.write_text(CONSUMER)
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(consumer)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
