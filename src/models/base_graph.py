"""
ООП-представление графа.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.models.data import EdgeData
from src.models.edge import Edge
from src.models.node import Node
from src.models.types import NodeKey, EmptyKey, Weight


@dataclass
class BaseGraph:
    """
    ООП-представление графа.
    """

    nodes: dict[NodeKey, Node]
    """
    Словарь узлов графа.
    """

    def __init__(self, edges: list[EdgeData] | None = None):
        self.nodes = {}

        if edges is not None:
            self.create_from_edges(edges)

    def create_from_edges(self, edges: list[EdgeData]) -> BaseGraph:
        """
        Создает граф из списка ребер.
        """
        for key_from, key_to, weight in edges:
            if key_to != EmptyKey:
                node_from = (
                    self.add(key_from)
                    if not self.contains(key_from)
                    else self.get(key_from)
                )
                node_to = (
                    self.add(key_to) if not self.contains(key_to) else self.get(key_to)
                )
                self.connect(node_from, node_to, weight)

        return self

    def get(self, key: NodeKey) -> Node:
        """
        Возвращает узел по его ключу.
        """
        return self.nodes[key]

    def contains(self, key: NodeKey) -> bool:
        """
        Проверяет, есть ли узел с таким ключом в графе.
        """
        return key in self.nodes

    def add(self, key: NodeKey) -> Node | None:
        """
        Добавляет узел в граф.
        """
        if key is EmptyKey:
            return None
        if self.contains(key):
            raise ValueError(f"Node with value {key} already exists")

        node = Node(key)
        self.nodes[key] = node

        return node

    @staticmethod
    def edge_exists(node_from: Node, node_to: Node) -> bool:
        """
        Проверяет, есть ли ребро между двумя узлами.
        """
        return node_to in node_from.parents

    def connect(self, node_from: Node, node_to: Node, weight: Weight) -> Edge | None:
        """
        Добавляет ребро в граф.
        """
        if self.edge_exists(node_from, node_to):
            raise ValueError(
                f"Edge from {node_from.key} to {node_to.key} already exists"
            )

        edge = Edge(node_to, weight)
        node_from.edges.append(edge)
        node_to.parents[node_from] = edge

        return edge
