from arrakisclient.client import ArrakisClient
from arrakisclient.types.namespace import ArrakisNamespace, Relation
from arrakisclient.types.tuple import ArrakisUserset


# Define some ORM-like models, must match the namespaces configured in the tenant
class ReferenceableNamespace(ArrakisNamespace):
    """Base model that will define the "ellipsis" relation, which can be used to reference items
    in the namespace as a unit, without implying any further relationships."""

    ellipsis = Relation(relation_name="...")


class User(ReferenceableNamespace):
    """ A model to represent users in your domain. """

    __namespace__ = "yourtenant/user"


class Document(ArrakisNamespace):
    """ A model to represent documents in your business domain (if you have such a thing). """

    __namespace__ = "yourtenant/document"

    # These relations define the permissions your code will ask about
    read = Relation(User)
    write = Relation(User)
    delete = Relation(User)

    # These relations define the relationship (role) a user can be directly granted
    viewer = Relation(User)
    contributor = Relation(User)
    owner = Relation(User)


token = "t_your_token_here_1234567deadbeef"
client = ArrakisClient(User, Document, access_token=token)

# Create some object references
a_doc = Document("doc1")
an_owner = User("theowner")
an_editor = User("userwhocanedit")
a_viewer = User("viewonlyuser")

# Insert some tuples granting roles to users
with client.batch_write() as w:
    w.create(a_doc.owner(an_owner.ellipsis))
    w.create(a_doc.contributor(an_editor.ellipsis))
    w.create(a_doc.viewer(a_viewer.ellipsis))

# Save the zookie that the call above generated to prevent new enemies
# We recommend saving this from any call to batch_write or content_change_check,
# and storing it alongside the object referenced in the write or check (in this case a_doc)"
when_perms_changed = w.revision

# Run some checks
assert client.check(a_doc.read, ArrakisUserset.from_onr(a_viewer.ellipsis), when_perms_changed)
assert client.check(a_doc.read, ArrakisUserset.from_onr(an_editor.ellipsis), when_perms_changed)
assert client.check(a_doc.read, ArrakisUserset.from_onr(an_owner.ellipsis), when_perms_changed)
assert not client.check(a_doc.write, ArrakisUserset.from_onr(a_viewer.ellipsis), when_perms_changed)
assert client.check(a_doc.write, ArrakisUserset.from_onr(an_editor.ellipsis), when_perms_changed)
assert client.check(a_doc.write, ArrakisUserset.from_onr(an_owner.ellipsis), when_perms_changed)
assert not client.check(
    a_doc.delete, ArrakisUserset.from_onr(a_viewer.ellipsis), when_perms_changed
)
assert not client.check(
    a_doc.delete, ArrakisUserset.from_onr(an_editor.ellipsis), when_perms_changed
)
assert client.check(a_doc.delete, ArrakisUserset.from_onr(an_owner.ellipsis), when_perms_changed)
