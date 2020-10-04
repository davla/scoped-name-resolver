from enum import Enum

from networkx import DiGraph


class NameGraph(DiGraph):
    pass


class NameNode:
    def __init__(self, namespace, name):
        self.namespace = namespace
        self.name = name


class ScopeNode:
    def __init__(self):
        pass


class ArcType(Enum):
    DEFINITION = 0
    IMPORT = 1
    NAMED_SCOPE = 2
    PARENT = 3
    REFERENCE = 4
    RESOLVED_IMPORT = 5
