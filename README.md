# Authzed-py

The Python client library for Authzed.

## Example Usage

### QuickStart

A complete version of this example can be found in this repository at [`examples/basic.py`](examples/basic.py)

In Python, we have support for declaring ORM-like models which allow you to easily interact with
the data in your tenant. Here we define some models for `User` and `Document` which match the
tenant namespace configuration.

```py
from arrakisclient.types.namespace import ArrakisNamespace, Relation


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
```

Now that we have our models, let's instantiate a client that will use them:

```py
from arrakisclient.client import ArrakisClient

token = "t_your_token_here_1234567deadbeef"
client = ArrakisClient(User, Document, access_token=token)
```

And now we can use our ORM-like models to mutate the data in the tenant:

```py
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
```

Now we can run some permissions checks on the date in the model to verify that it matches our expectations:

```py
from arrakisclient.types.tuple import ArrakisUserset

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
```
