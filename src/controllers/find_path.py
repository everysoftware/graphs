"""
Поиск пути между двумя вершинами.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.node import Node
    from src.models.types import NodeKey


def find_path(
    start: Node,
    end: Node,
    visited: set[NodeKey] | None = None,
    path: list[NodeKey] | None = None,
) -> list[NodeKey] | None:
    if visited is None:
        visited = set()
    if path is None:
        path = []

    path.append(start.key)
    visited.add(start.key)

    if start == end:
        return path

    for edge in start.edges:
        if edge.adjacent.key not in visited:
            if find_path(edge.adjacent, end, visited, path):
                return path

    return []


def find_path_wrapper(start: Node, end: Node) -> list[NodeKey]:
    return find_path(start, end)
