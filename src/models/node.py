from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.edge import Edge
    from src.models.types import NodeKey


@dataclass
class Node:
    """
    Узел графа.
    """

    key: NodeKey
    """Значение узла."""
    edges: list[Edge]
    """Список рёбер, ведущих из узла."""
    parents: dict[Node, Edge]
    """Список родителей."""

    def __init__(self, value: NodeKey):
        self.key = value
        self.edges = []
        self.parents = {}

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other: Node):
        return self.key == other.key

    def __repr__(self):
        return f"Node({self.key})"
