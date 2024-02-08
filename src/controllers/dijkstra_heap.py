"""
Нахождение кратчайшего пути во взвешанном графе.
"""

from __future__ import annotations

import heapq
from typing import TYPE_CHECKING

from src.models.types import NodeKey

if TYPE_CHECKING:
    from src.controllers.graph import Graph
    from src.models.node import Node

"""
Разница в сложности между использованием кучи и не использованием кучи в алгоритме Дейкстры. 

1. **С кучей**: Когда мы используем кучу, мы можем извлекать вершину с минимальным расстоянием за время O(log V). 
Так как мы делаем это для каждой вершины и каждого ребра, общая сложность составляет O((V+E) log V).

2. **Без кучи**: Когда мы не используем кучу, мы должны просматривать все непосещенные вершины, чтобы найти вершину
 с минимальным расстоянием. Это требует O(V) операций для каждой вершины, поэтому общая сложность составляет O(V^2). 
 Мы также должны рассмотреть каждое ребро один раз, что добавляет O(E) к общей сложности, делая ее O(V^2 + E).

Ваш вопрос о сложности O((V+E)V) интересен. Эта сложность могла бы быть, если бы мы просматривали все вершины для
 каждого ребра, но это не то, что происходит в алгоритме Дейкстры. В алгоритме Дейкстры мы просматриваем все вершины
только один раз (что дает сложность O(V^2)), а затем просматриваем все ребра (что дает сложность O(E)). 
Поэтому общая сложность без использования кучи составляет O(V^2 + E), а не O((V+E)V).
"""


def extract_path(previous: dict[Node, Node], start: Node, end: Node) -> list[NodeKey]:
    path = []
    current_node = end

    while current_node != start:
        path.append(current_node.key)
        current_node = previous[current_node]

    path.append(start.key)
    return path[::-1]


def dijkstra_heap(graph: Graph, start: Node, end: Node) -> list[NodeKey]:
    """
    Алгоритм Дейкстры на куче.

    Сложность алгоритма: O((V + E) * log(V))
    """
    time = {node: float("inf") for node in graph.nodes.values()}
    time[start] = 0
    previous = {}
    queue = [(0, start)]

    while queue:
        # O(logN) для каждой вершины = O(V * log(V))
        current_time, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        if current_time > time[current_node]:
            continue

        # O(logN) для каждого ребра = O(E * log(V))
        for edge in current_node.edges:
            new_time = current_time + edge.weight
            if new_time < time[edge.adjacent]:
                time[edge.adjacent] = new_time
                previous[edge.adjacent] = current_node
                heapq.heappush(queue, (new_time, edge.adjacent))

    if time[end] == float("inf"):
        return []

    return extract_path(previous, start, end)


def dijkstra_heap_wrapper(graph: Graph, start: Node, end: Node) -> list[NodeKey]:
    return dijkstra_heap(graph, start, end)
