from typing import Iterable, Dict, Tuple

from . import NBL_AST, identity
from .model import ExplorationTree, PatternBindings, namegraph


class GraphBuilder:
    Match = Tuple[Dict[str, object], Iterable[NBL_AST.Clause]]

    @staticmethod
    def match_rule(node: ExplorationTree, nbl_rules: Iterable[NBL_AST.Rule]) \
            -> __class__.Match:
        matches = (
            (node.match(rule.pattern), rule.clauses)
            for rule in nbl_rules
        )
        return next(
                match
                for match in matches
                if match[0]
        )

    def _build_Define(self, clause: NBL_AST.Defines, matches: PatternBindings)\
            -> namegraph.NameGraph:
        var_name = matches[clause.variable.name]
        name_node = namegraph.NameNode(clause.variable.namespace, var_name)
        self.graph.add_edge(self.current_scope, name_node,
                            type=namegraph.ArcType.DEFINITION)
        return self.graph

    def _build_Scopes(self, clause: NBL_AST.Scopes, matches: PatternBindings) \
            -> namegraph.NameGraph:
        scope_node = namegraph.ScopeNode()
        self.graph.add_edge(scope_node, self.current_scope,
                            type=namegraph.ArcType.PARENT)
        self.current_scope = scope_node
        return self.graph

    def _build(self, clause: NBL_AST.Clause, matches: PatternBindings) \
            -> namegraph.NameGraph:
        clause_class_name = clause.__class__.__name__
        method = getattr(self, '_build_' + clause_class_name, identity)
        return method(clause, matches)

    def __init__(self, tree: ExplorationTree,
                 nbl_rules: Iterable[NBL_AST.Rule],
                 graph=namegraph.NameGraph(),
                 scope=namegraph.ScopeNode()):
        self.tree = tree
        self.rules = nbl_rules
        self.graph = graph
        self.current_scope = scope

    def build(self):
        matches, clauses = self.match_rule(self.tree, self.rules)

        for clause in clauses:
            self._build(clause, matches)

        for child in self.tree.children():
            builder = GraphBuilder(child, self.rules, self.graph,
                                   self.current_scope)
            builder.build()

        return self.graph


def build(tree: ExplorationTree, nbl_rules: Iterable[NBL_AST.Rule]) \
        -> namegraph.NameGraph:
    return GraphBuilder(tree, nbl_rules).build()


