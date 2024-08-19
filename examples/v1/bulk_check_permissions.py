from authzed.api.v1 import (
    BulkCheckPermissionRequest,
    BulkCheckPermissionRequestItem,
    CheckPermissionResponse,
    Client,
    Consistency,
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

resp = client.BulkCheckPermission(
    BulkCheckPermissionRequest(
        consistency=Consistency(fully_consistent=True),
        items=[
            BulkCheckPermissionRequestItem(
                resource=post_one,
                permission="view",
                subject=beatrice,
            ),
            BulkCheckPermissionRequestItem(
                resource=post_one,
                permission="write",
                subject=beatrice,
            ),
        ],
    )
)
assert len(resp.pairs) == 2
assert (
    resp.pairs[0].item.permissionship
    == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION
)
assert (
    resp.pairs[1].item.permissionship
    == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION
)
