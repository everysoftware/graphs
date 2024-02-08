"""
Нахождение кратчайшего пути во взвешанном графе.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.models.types import Weight, NodeKey

if TYPE_CHECKING:
    from src.controllers.graph import Graph
    from src.models.node import Node


def init_hash_tables(
    graph: Graph, unprocessed: set[Node], time: dict[Node, Weight | float], start: Node
) -> None:
    for node in graph.nodes.values():
        unprocessed.add(node)
        time[node] = float("inf")

    time[start] = 0


def calculate_time(
    unprocessed: set[Node], time: dict[Node, Weight | float], previous: dict[Node, Node]
) -> None:
    while unprocessed:
        # O(V) для каждой вершины = O(V^2)
        current_node = min(unprocessed, key=lambda node: time[node])

        if time[current_node] == float("inf"):
            break

        unprocessed.remove(current_node)

        # O(1) для каждого ребра = O(E)
        for edge in current_node.edges:
            if edge.adjacent in unprocessed:
                new_time = time[current_node] + edge.weight

                if new_time < time[edge.adjacent]:
                    time[edge.adjacent] = new_time
                    previous[edge.adjacent] = current_node


def extract_path(previous: dict[Node, Node], start: Node, end: Node) -> list[NodeKey]:
    path = []
    current_node = end

    while current_node != start:
        path.append(current_node.key)
        current_node = previous[current_node]

    path.append(start.key)
    return path[::-1]


def dijkstra(graph: Graph, start: Node, end: Node) -> list[NodeKey]:
    """
    Алгоритм Дейкстры.

    Сложность алгоритма: O(V^2 + E)
    """
    unprocessed = set()
    time = {}
    previous = {}
    init_hash_tables(graph, unprocessed, time, start)
    calculate_time(unprocessed, time, previous)

    if time[end] == float("inf"):
        return []

    return extract_path(previous, start, end)


def dijkstra_wrapper(graph: Graph, start: Node, end: Node) -> list[NodeKey]:
    return dijkstra(graph, start, end)
