import pytest

from authzed.api.v1 import ObjectReference, Relationship


def test_type_error_does_not_segfault():
    with pytest.raises(TypeError):
        res = ObjectReference(object_type="post", object_id="post-one")
        Relationship(
            resource=res,
            relation="writer",
            subject=res,
        )
