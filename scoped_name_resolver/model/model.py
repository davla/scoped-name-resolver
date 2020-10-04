from typing import Dict, Iterable

from scoped_name_resolver import NBL_AST

PatternBindings = Dict[str, object]

class ExplorationTree:
    def __init__(self):
        pass

    def __getattr__(self, item: str):
        raise NotImplementedError

    def children(self) -> Iterable[__class__]:
        raise NotImplementedError

    def match(self, nbl_pattern: NBL_AST.Pattern) -> PatternBindings:
        raise NotImplementedError


