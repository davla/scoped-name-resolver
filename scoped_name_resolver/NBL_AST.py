from typing import Iterable


class Namespace:
    def __init__(self, name: str):
        self.name = name


class Pattern:
    def __init__(self, node_name: str, fields: Iterable[str]):
        self.node_name = node_name
        self.fields = fields


class NamespacesDecl:
    def __init__(self, namespaces: Iterable[Namespace]):
        self.namespaces = namespaces


class Variable:
    def __init__(self, name: str, namespace: Namespace):
        self.name = name
        self.namespace = namespace


class Clause:
    def __init__(self):
        pass


class Rule:
    def __init__(self, pattern: Pattern, clauses: Iterable[Clause]):
        self.pattern = pattern
        self.clauses = clauses


class RefClause(Clause):
    def __init__(self, var_name: str):
        super().__init__()
        self.var_name = var_name


class Scopes(Clause):
    def __init__(self, namespaces: Iterable[Namespace]):
        super().__init__()
        self.namespaces = namespaces


class VarClause(Clause):
    def __init__(self, variable: Variable):
        super().__init__()
        self.variable = variable


class In(RefClause):
    def __init__(self, var_name: str):
        super().__init__(var_name)


class Where(RefClause):
    def __init__(self, var_name: str, subclause: Clause):
        super().__init__(var_name)
        self.subclause = subclause


class Defines(VarClause):
    def __init__(self, variable: Variable, unique=False):
        super().__init__(variable)
        self.unique = unique


class Otherwise(VarClause):
    def __init__(self, variable: Variable):
        super().__init__(variable)


class Refers(VarClause):
    def __init__(self, variable: Variable, elses: Iterable[Otherwise]=(),
                 within: In=None, where: Where=None):
        super().__init__(variable)
        self.elses = elses
        self.within = within
        self.where = where
