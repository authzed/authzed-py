import grpc
import grpc.aio
import pytest
from protovalidate import ValidationError, validate

from authzed.api.v1 import ObjectReference, Relationship
from grpcutil import AuthzedError


def test_authzed_error_catches_sync_and_async_grpc_errors():
    # The sync client raises grpc.RpcError; the async client raises
    # grpc.aio.AioRpcError. AuthzedError must catch both.
    with pytest.raises(AuthzedError):
        raise grpc.RpcError("sync error")

    assert issubclass(grpc.RpcError, AuthzedError)
    assert issubclass(grpc.aio.AioRpcError, AuthzedError)


def test_type_error_does_not_segfault():
    with pytest.raises(TypeError):
        res = ObjectReference(object_type="post", object_id="post-one")
        Relationship(
            resource=res,
            relation="writer",
            subject=res,
        )


def test_validate():
    with pytest.raises(ValidationError):
        validate(ObjectReference(object_type="post", object_id="@#¢∞¬÷“”"))

    validate(ObjectReference(object_type="post", object_id="test"))
