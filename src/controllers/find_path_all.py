"""
Поиск всех путей между двумя вершинами.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.node import Node
    from src.models.types import NodeKey


def find_path_all(
    start: Node,
    end: Node,
    visited: set[NodeKey] | None = None,
    path: list[NodeKey] | None = None,
    paths: list[list[NodeKey]] | None = None,
) -> None:
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if paths is None:
        paths = []

    path.append(start.key)
    visited.add(start.key)

    if start == end:
        paths.append(path.copy())

    for edge in start.edges:
        if edge.adjacent.key not in visited:
            find_path_all(edge.adjacent, end, visited, path, paths)

    visited.remove(start.key)
    path.pop()


def find_path_all_wrapper(start: Node, end: Node) -> list[list[NodeKey]]:
    paths = []
    find_path_all(start, end, paths=paths)
    return paths
