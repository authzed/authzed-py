import re

_IDENTIFIER = r"[a-z][a-z0-9_]{2,62}[a-z0-9]"
NAMESPACE_NAME_REGEX = fr"^({_IDENTIFIER}/)?{_IDENTIFIER}$"
RELATION_NAME_REGEX = fr"^{_IDENTIFIER}$"
SPECIAL_RELATION_NAMES = {"..."}


def validate_namespace_name(namespace_name: str) -> bool:
    """ Validates that the namespace name given conforms to the rules. """
    return bool(re.match(NAMESPACE_NAME_REGEX, namespace_name))


def validate_relation_name(relation_name: str) -> bool:
    """ Validates that the relation name given conforms to the rules. """
    return (
        bool(re.match(RELATION_NAME_REGEX, relation_name))
        or relation_name in SPECIAL_RELATION_NAMES
    )
