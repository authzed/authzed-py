from authzed.api.v1 import WriteSchemaRequest

from .utils import maybe_await


async def write_test_schema(client):
    schema = """
        caveat likes_harry_potter(likes bool) {
          likes == true
        }

        definition post {
            relation writer: user
            relation reader: user
            relation caveated_reader: user with likes_harry_potter

            permission write = writer
            permission view = reader + writer
            permission view_as_fan = caveated_reader + writer
        }
        definition user {}
    """
    await maybe_await(client.WriteSchema(WriteSchemaRequest(schema=schema)))
