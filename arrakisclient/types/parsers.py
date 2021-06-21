from typing import Dict

import google.protobuf.text_format

import authzed.api.v0.namespace_pb2 as ns_proto


class NamespaceConfigParseException(Exception):
    """ Exception raised when a namespace fails to parse. """


def parse_namespace_config(namespace_config_text) -> ns_proto.NamespaceDefinition:
    """Parses the specified namespace configuration, raising a NamespaceConfigParseException
    on error and otherwise returning the parsed namespace proto.
    """
    parsed = ns_proto.NamespaceDefinition()
    try:
        google.protobuf.text_format.Parse(namespace_config_text, parsed)
        assert len(parsed.name) > 0
    except AssertionError as ex:
        raise NamespaceConfigParseException from ex
    except google.protobuf.text_format.ParseError as pe:
        raise NamespaceConfigParseException from pe

    return parsed


def relation_map(parsed: ns_proto.NamespaceDefinition) -> Dict[str, ns_proto.Relation]:
    """Builds a map from relation name to the root node of the relation. If duplicate
    entries are found, the last found is used.
    """
    return {relation.name: relation for relation in parsed.relation}
