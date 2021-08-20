from authzed.api.v0 import CheckRequest, Client, ObjectAndRelation, User
from grpcutil import bearer_token_credentials

emilia = User("blog/user", "emilia")
beatrice = User("blog/user", "beatrice")

post_one_reader = ObjectAndRelation(
    namespace="blog/post",
    object_id="1",
    relation="reader",
)
post_one_writer = ObjectAndRelation(
    namespace="blog/post",
    object_id="1",
    relation="writer",
)

client = Client("grpc.authzed.com:443", bearer_token_credentials("mytoken"))

resp = client.Check(CheckRequest(test_userset=post_one_reader, user=emilia))
assert resp.is_member
resp = client.Check(CheckRequest(test_userset=post_one_writer, user=emilia))
assert resp.is_member
resp = client.Check(CheckRequest(test_userset=post_one_reader, user=beatrice))
assert resp.is_member
resp = client.Check(CheckRequest(test_userset=post_one_writer, user=beatrice))
assert not resp.is_member
