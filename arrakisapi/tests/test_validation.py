import pytest
from arrakisapi.validation import (validate_namespace_name,
                                   validate_relation_name)


@pytest.mark.parametrize(
    "namespace_name, is_valid",
    [
        ("", False),
        ("a", False),
        ("foo", False),
        ("bar", False),
        ("foo1", True),
        ("bar1", True),
        ("foo_bar", True),
        ("foo_bar_", False),
        ("ab", False),
        ("Foo", False),
        ("foo1/bar1", True),
        ("foo1/b", False),
        ("Foo1/bar1", False),
        ("foo1/bar1/baz1", False),
        ("f" * 3, False),
        ("f" * 4, True),
        ("\u0394" * 4, False),
        ("\n" * 4, False),
        ("_" * 4, False),
        ("-" * 4, False),
        ("/" * 4, False),
        ("\\" * 4, False),
        ("f" * 64, True),
        ("f" * 65, False),
        (f"{'f' * 63}/{'f' * 63}", True),
        (f"{'f' * 64}/{'f' * 64}", True),
        (f"{'f' * 65}/{'f' * 64}", False),
        (f"{'f' * 64}/{'f' * 65}", False),
    ],
)
def test_validate_namespace_name(namespace_name, is_valid):
    assert validate_namespace_name(namespace_name) == is_valid


@pytest.mark.parametrize(
    "relation_name, is_valid",
    [
        ("", False),
        ("...", True),
        ("foo", False),
        ("bar", False),
        ("foo1", True),
        ("bar1", True),
        ("ab", False),
        ("Foo1", False),
        ("foo_bar", True),
        ("foo_bar_", False),
        ("foo/bar", False),
        ("foo/b", False),
        ("Foo/bar", False),
        ("foo/bar/baz", False),
        ("f" * 3, False),
        ("f" * 4, True),
        ("\u0394" * 4, False),
        ("\n" * 4, False),
        ("_" * 4, False),
        ("-" * 4, False),
        ("/" * 4, False),
        ("\\" * 4, False),
        ("f" * 64, True),
        (f"{'f' * 63}/{'f' * 63}", False),
        (f"{'f' * 64}/{'f' * 64}", False),
        (f"{'f' * 65}/{'f' * 64}", False),
        (f"{'f' * 64}/{'f' * 65}", False),
        ("f" * 65, False),
    ],
)
def test_validate_relation_name(relation_name, is_valid):
    assert validate_relation_name(relation_name) == is_valid
