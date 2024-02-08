"""
BFS - Breadth First Search (поиск в ширину)
"""

from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

from src.models.types import NodeKey

if TYPE_CHECKING:
    from src.controllers.graph import Graph
    from src.models.node import Node

"""
Обход графа в ширину (BFS - Breadth First Search) - это алгоритм обхода или поиска данных в графе, который
исследует соседние узлы первого уровня, а затем исследует узлы следующего уровня, которые могут быть достигнуты
только после исследования узлов первого уровня. BFS исследует все узлы на одном уровне перед переходом к следующему
уровню.

Сложность алгоритма: O(V + E), где V - количество вершин, E - количество рёбер.
"""


def bfs(
    node: Node, visited: set[NodeKey] | None = None, result: list[NodeKey] | None = None
) -> list[NodeKey]:
    """
    Обход графа в ширину (только связные графы).
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []

    queue = deque([node])

    while queue:
        node = queue.popleft()
        visited.add(node.key)
        result.append(node.key)

        for edge in node.edges:
            if edge.adjacent.key not in visited:
                visited.add(edge.adjacent.key)
                queue.append(edge.adjacent)

    return result


def bfs_wrapper(graph: Graph) -> list[NodeKey]:
    """
    Обход графа в ширину.
    """
    visited = set()
    result = []

    for node in graph.nodes.values():
        if node.key not in visited:
            bfs(node, visited, result)

    return result
