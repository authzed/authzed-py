import pytest
from protovalidate import ValidationError, validate

from authzed.api.v1 import ObjectReference, Relationship


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
