from .model import ExplorationTree
from .graph_builder import GraphBuilder, build

name = 'scoped_name_resolver'


def identity(*args):
    return args
