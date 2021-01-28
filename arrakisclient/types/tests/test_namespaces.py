from typing import Set, Type

from arrakisclient.types.namespace import ArrakisNamespace, Relation


class ReferenceableNamespace(ArrakisNamespace):
    ellipsis = Relation(relation_name="...")


class User(ReferenceableNamespace):
    __namespace__ = "testtenant/user"


class UserGroup(ArrakisNamespace):
    __namespace__ = "testtenant/usergroup"

    admin = Relation(User)
    member = Relation(User)


class ViewableEditable(ArrakisNamespace):
    view = Relation(UserGroup)
    edit = Relation(UserGroup)


class Deletable(ArrakisNamespace):
    delete = Relation(UserGroup)


class Document(ViewableEditable, Deletable):
    __namespace__ = "testtenant/document"


def relations(ns: Type[ArrakisNamespace]) -> Set[str]:
    return {rel.relation_name for rel in ns.__relations__}


def test_inherited_relations():
    assert "..." in relations(User)
    assert "admin" in relations(UserGroup)
    assert "member" in relations(UserGroup)
    assert "view" in relations(Document)
    assert "edit" in relations(Document)
    assert "delete" in relations(Document)


def test_relation_parent_class():
    assert "User" == User.ellipsis.parent_class_name
    assert "ViewableEditable" == ViewableEditable.view.parent_class_name
    assert "Document" == Document.delete.parent_class_name
