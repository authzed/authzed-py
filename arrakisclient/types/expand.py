from enum import IntEnum
from typing import Dict, Iterable, Optional, Type

import authzed.api.v0.core_pb2 as core_proto
from arrakisclient.types.namespace import ArrakisNamespace
from arrakisclient.types.tuple import ArrakisUser, ObjectAndRelation


class ExpandOperation(IntEnum):
    UNION = 1
    INTERSECTION = 2
    EXCLUSION = 3


_EXPAND_OPERATION_MAP: Dict[int, ExpandOperation] = {
    core_proto.SetOperationUserset.UNION: ExpandOperation.UNION,
    core_proto.SetOperationUserset.INTERSECTION: ExpandOperation.INTERSECTION,
    core_proto.SetOperationUserset.EXCLUSION: ExpandOperation.EXCLUSION,
}


class ExpandTree(object):
    """
    ExpandTree represents an expanded relation.

    Expanded relations can have direct results and results that must be
    computed from ExpandOperations and a tree of results.
    """

    def __init__(
        self,
        tree: core_proto.RelationTupleTreeNode,
        ns_map: Dict[str, Type[ArrakisNamespace]],
        onr: ObjectAndRelation = None,
    ):
        assert tree != core_proto.RelationTupleTreeNode()
        self._tree = tree
        self._onr = ObjectAndRelation.from_proto(tree.expanded, ns_map) if onr is None else onr
        self._ns_map = ns_map
        self._subtree_lookup = (
            {subtree.object_and_relation: subtree for subtree in self.set_operation_children}
            if not self.is_leaf
            else None
        )

    def find(self, onr: ObjectAndRelation) -> "Optional[ExpandTree]":
        """Finds the sub tree for the given object and relation in this tree and
        returns it or None if none.
        """
        if self.is_leaf:
            return None

        if self._subtree_lookup and self._subtree_lookup.get(onr):
            return self._subtree_lookup[onr]

        for subtree in self.set_operation_children:
            found = subtree.find(onr)
            if found is not None:
                return found

        return None

    @property
    def operation(self) -> ExpandOperation:
        assert not self.is_leaf
        return _EXPAND_OPERATION_MAP[self._tree.intermediate_node.operation]

    @property
    def object_and_relation(self) -> ObjectAndRelation:
        """
        The context from which the current tree expansion was created.
        This is different from the `object_and_relation` property because
        direct member leafs return their parent's relation.

        Excluding `this_` relations, the return value is the ObjectAndRelation
        that, when expanded, produces this tree.
        """
        return self._onr

    @property
    def is_leaf(self) -> bool:
        return self._tree.HasField("leaf_node")

    @property
    def leaf_children(self) -> Iterable[ArrakisUser]:
        assert self.is_leaf
        return _leaf_to_iterable(self._tree.leaf_node, self._ns_map)

    @property
    def set_operation_children(self) -> "Iterable[ExpandTree]":
        assert not self.is_leaf
        for subtree in self._tree.intermediate_node.child_nodes:
            onr = (
                self.object_and_relation.this_
                if subtree.expanded == core_proto.ObjectAndRelation()
                else None
            )
            yield ExpandTree(subtree, self._ns_map, onr=onr)

    @property
    def flattened_children(self) -> Iterable[ArrakisUser]:
        if self.is_leaf:
            return self.leaf_children

        children_nodes = list(self.set_operation_children)
        if len(children_nodes) == 0:
            return {}

        results = set(children_nodes[0].flattened_children)
        for child_set in children_nodes[1:]:
            children = child_set.flattened_children
            if self.operation == ExpandOperation.UNION:
                results.update(children)
            elif self.operation == ExpandOperation.INTERSECTION:
                results.intersection_update(children)
            elif self.operation == ExpandOperation.EXCLUSION:
                results.difference_update(children)
            else:
                raise NotImplementedError()

        return results

    def __getitem__(self, onr: ObjectAndRelation) -> "ExpandTree":
        return self._subtree_lookup[onr]


def _leaf_to_iterable(
    leaf: core_proto.DirectUserset, ns_map: Dict[str, Type[ArrakisNamespace]]
) -> Iterable[ArrakisUser]:
    for user in leaf.users:
        yield ObjectAndRelation.from_proto(user.userset, ns_map).as_userset()
