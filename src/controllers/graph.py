from __future__ import annotations

from src.controllers.bfs import bfs_wrapper, bfs
from src.controllers.dfs import dfs_iterative, dfs_wrapper, dfs
from src.controllers.dijkstra import dijkstra_wrapper
from src.controllers.dijkstra_heap import dijkstra_heap_wrapper
from src.controllers.find_path import find_path_wrapper
from src.controllers.find_path_all import find_path_all_wrapper
from src.controllers.find_shortest_path import find_shortest_path_wrapper
from src.models.base_graph import BaseGraph
from src.models.node import Node
from src.models.types import NodeKey


class Graph(BaseGraph):
    def dfs(self, node: Node | None = None) -> list[NodeKey]:
        """
        Обход графа в глубину.
        """
        return dfs_wrapper(self) if node is None else dfs(node)

    def dfs_iterative(self, node: Node | None = None) -> list[NodeKey]:
        """
        Обход графа в глубину с использованием стека.
        """
        return (
            dfs_wrapper(self, helper=dfs_iterative)
            if node is None
            else dfs_iterative(node)
        )

    @staticmethod
    def find_path(start: Node, end: Node) -> list[NodeKey]:
        """
        Находит путь между двумя узлами.
        """
        return find_path_wrapper(start, end)

    @staticmethod
    def find_path_all(start: Node, end: Node) -> list[list[NodeKey]]:
        """
        Находит все пути между двумя узлами.
        """
        return find_path_all_wrapper(start, end)

    def bfs(self, node: Node | None = None) -> list[NodeKey]:
        """
        Обход графа в ширину.
        """
        return bfs_wrapper(self) if node is None else bfs(node)

    @staticmethod
    def find_shortest_path(start: Node, end: Node) -> list[NodeKey]:
        """
        Находит кратчайший путь между двумя узлами.
        """
        return find_shortest_path_wrapper(start, end)

    def dijkstra(self, start: Node, end: Node) -> list[NodeKey]:
        """
        Алгоритм Дейкстры.
        """
        return dijkstra_wrapper(self, start, end)

    def dijkstra_heap(self, start: Node, end: Node) -> list[NodeKey]:
        """
        Алгоритм Дейкстры с использованием кучи.
        """
        return dijkstra_heap_wrapper(self, start, end)
