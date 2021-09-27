from authzed.api.v1 import (
    CheckPermissionRequest,
    CheckPermissionResponse,
    Client,
    ObjectReference,
    SubjectReference,
)
from grpcutil import bearer_token_credentials

emilia = SubjectReference(
    object=ObjectReference(
        object_type="blog/user",
        object_id="emilia",
    )
)
beatrice = SubjectReference(
    object=ObjectReference(
        object_type="blog/user",
        object_id="beatrice",
    )
)

post_one = ObjectReference(object_type="blog/post", object_id="1")

client = Client(
    "grpc.authzed.com:443",
    bearer_token_credentials("t_your_token_here_1234567deadbeef"),
)

resp = client.CheckPermission(
    CheckPermissionRequest(
        resource=post_one,
        permission="reader",
        subject=emilia,
    )
)
assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

resp = client.CheckPermission(
    CheckPermissionRequest(
        resource=post_one,
        permission="writer",
        subject=emilia,
    )
)
assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

resp = client.CheckPermission(
    CheckPermissionRequest(
        resource=post_one,
        permission="reader",
        subject=beatrice,
    )
)
assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

resp = client.CheckPermission(
    CheckPermissionRequest(
        resource=post_one,
        permission="writer",
        subject=beatrice,
    )
)
