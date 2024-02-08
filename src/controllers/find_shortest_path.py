"""
Нахождение кратчайшего пути в невзвешанном графе.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.models.types import NodeKey

if TYPE_CHECKING:
    from src.models.node import Node


@dataclass
class PathNode:
    """
    Узел пути.
    """

    node: Node
    """Узел."""
    parent: PathNode | None
    """Родительский узел."""

    def __repr__(self):
        return f"PathNode({self.node})"


def extract_path(path_node: PathNode) -> list[NodeKey]:
    """
    Извлечение пути.
    """
    path = []
    while path_node:
        path.append(path_node.node.key)
        path_node = path_node.parent
    return path[::-1]


"""
Поиска кратчайшего пути в невзвешанном графе.

Принцип работы:
BFS сначала проверяет все вершины на расстоянии 1 от начальной вершины, затем все вершины на расстоянии 2, и так далее. 
Это означает, что когда BFS достигает конечной вершины, он уже проверил все возможные пути к ней, которые короче. 
Поэтому первый найденный путь до конечной вершины гарантированно будет кратчайшим.
"""


def find_shortest_path(
    start: Node, end: Node, visited: list[NodeKey] | None = None
) -> list[NodeKey]:
    if visited is None:
        visited = set()

    queue = deque([PathNode(start, None)])

    while queue:
        path_node = queue.popleft()
        visited.add(path_node.node.key)

        # Если найден конечный узел, то возвращаем путь.
        if path_node.node == end:
            return extract_path(path_node)

        for edge in path_node.node.edges:
            if edge.adjacent.key not in visited:
                # Оптимизация: если смежный узел является конечным, то кладем его в начало очереди.
                if edge.adjacent == end:
                    queue.appendleft(PathNode(edge.adjacent, path_node))
                    continue

                visited.add(edge.adjacent.key)
                queue.append(PathNode(edge.adjacent, path_node))

    return []


def find_shortest_path_wrapper(start: Node, end: Node) -> list[NodeKey]:
    return find_shortest_path(start, end)
