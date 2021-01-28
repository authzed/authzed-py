import pytest

from arrakisclient.types.parsers import NamespaceConfigParseException, parse_namespace_config


@pytest.mark.parametrize(
    "config, expected_name",
    [
        pytest.param("", None, id="empty"),
        pytest.param(
            """
            name: foo
            """,
            None,
            id="missing-quotes",
        ),
        pytest.param(
            """
            name: foo
            relation { name: "owner"
            """,
            None,
            id="missing-brace",
        ),
        pytest.param(
            """
            name: foo
            relation: { name: "owner" }
            """,
            None,
            id="extra-colon",
        ),
        pytest.param(
            """
                  name:                     "doc"
            relation:          {       name:
            "owner" 
                             }
            """,
            "doc",
            id="wacky-spacing",
        ),
        pytest.param(
            """
            name: "doc"
            """,
            "doc",
            id="valid-empty",
        ),
        pytest.param(
            """
            name: "doc"  # This is a comment
            """,
            "doc",
            id="has-comment",
        ),
        pytest.param(
            """
            name: "foobar"
            relation { name: "owner" }
            """,
            "foobar",
            id="single-relation",
        ),
        pytest.param(
            """
            name: "foobar"
            relation { name: "owner" }
            relation { name: "editor" }
            """,
            "foobar",
            id="multiple-relations",
        ),
        pytest.param(
            """
            name: "editor"
            relation {
                name: "editor"
                userset_rewrite {
                    union {
                        child { _this {} }
                        child { computed_userset { relation: "owner" } }
                    }
                }
            }
            """,
            "editor",
            id="single-rewrite",
        ),
        pytest.param(
            """
            name: "editor"
            relation {
                name: "editor"
                userset_rewrite {
                    exclusion {
                        child {
                            userset_rewrite {
                                union {
                                    child { _this {} }
                                    child { computed_userset { relation: "owner" } }
                                }
                            }
                        }
                        child {
                            userset_rewrite {
                                intersection {
                                    child { computed_userset { relation: "threestrikes" } }
                                    child { computed_userset { relation: "blacklisted" } }
                                }
                            }
                        }
                    }
                }
            }
            """,
            "editor",
            id="nested-rewrite",
        ),
        pytest.param(
            """
            name: "editor"
            relation {
                name: "editor"
                userset_rewrite {
                    union {
                        child { _this {} }
                        child { computed_userset { relation: "owner" } }
                    }
                }
            }

            relation {
                name: "viewer"
                userset_rewrite {
                    union {
                        child { _this {} }
                        child { computed_userset { relation: "editor" } }
                    }
                }
            }
            """,
            "editor",
            id="multiple-rewrite",
        ),
        pytest.param(
            """
            name: "something"

            relation { name: "owner" }
            relation {
                name: "editor"
                userset_rewrite {
                    union {
                        child { _this {} }
                        child { computed_userset { relation: "owner" } }
                    }
                }
            }

            relation {
                name: "viewer"
                userset_rewrite {
                    union {
                        child { _this {} }
                        child { computed_userset { relation: "editor" } }
                        child {
                            tuple_to_userset {
                                tupleset { relation: "parent" }
                                computed_userset {
                                    object: TUPLE_USERSET_OBJECT # parent folder
                                    relation: "viewer"
                                }
                            }
                        }
                    }
                }
            }
            """,
            "something",
            id="complicated-rewrite",
        ),
        pytest.param(
            """
            name: "something"

            relation { name: "owner" }
            relation {
                name: "editor"
                userset_rewrite {
                    union {
                        child { _this {} }
                        child { computed_userset { relation: "owner" } }
                    }
                }
            }

            relation {
                name: "viewer"
                userset_rewrite {
                    union {
                        child { _this {} }
                        child { computed_userset { relation: "editor" } # Missing brace here!
                        child {
                            tuple_to_userset {
                                tupleset { relation: "parent" }
                                computed_userset {
                                    object: TUPLE_USERSET_OBJECT # parent folder
                                    relation: "viewer"
                                }
                            }
                        }
                    }
                }
            }
            """,
            None,
            id="large-and-broken",
        ),
    ],
)
def test_parsing(config, expected_name):
    try:
        parsed = parse_namespace_config(config)
        assert parsed.name == expected_name
    except NamespaceConfigParseException:
        assert expected_name is None
