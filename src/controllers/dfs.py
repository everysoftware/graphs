"""
Обход графа в глубину (DFS - Depth First Search)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from src.models.types import NodeKey

if TYPE_CHECKING:
    from src.controllers.graph import Graph
    from src.models.node import Node

"""
Обход графа в глубину (DFS - Depth First Search) - это алгоритм обхода или поиска данных в графе, который исследует
ветви графа до тех пор, пока не найдет целевой узел или не достигнет конца графа. В отличие от BFS, который исследует
соседние узлы первого уровня, DFS исследует узлы до тех пор, пока не достигнет конца ветви, а затем возвращается к
предыдущему узлу и исследует другую ветвь.

Сложность алгоритма: O(V + E), где V - количество вершин, E - количество рёбер.
"""


def dfs(
    node: Node, visited: set[NodeKey] | None = None, result: list[NodeKey] | None = None
) -> list[NodeKey]:
    """
    Обход графа в глубину (только связные графы).
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []

    # Посещение вершин даёт сложность O(V)
    visited.add(node.key)
    result.append(node.key)

    # Цикл перебора рёбер даёт сложность O(E)
    for edge in node.edges:
        if edge.adjacent.key not in visited:
            dfs(edge.adjacent, visited, result)

    return result


"""
Итеративный обход в глубину (DFS) немного отличается от рекурсивного. 
Вместо того чтобы использовать стек вызовов функций (как в рекурсивном DFS), итеративный DFS явно использует свой 
собственный стек.

Вот основные шаги итеративного DFS:

1. Начинается с заданной вершины (назовем ее начальной вершиной), которая добавляется в стек.
2. Затем извлекается вершина из верхней части стека. Если эта вершина еще не была посещена, она добавляется в 
список посещенных вершин.
3. Затем все соседние вершины текущей вершины, которые еще не были посещены, добавляются в стек.
4. Шаги 2 и 3 повторяются до тех пор, пока стек не станет пустым.
"""


def dfs_iterative(
    node: Node, visited: set[NodeKey] | None = None, result: list[NodeKey] | None = None
) -> list[NodeKey]:
    """
    Итеративный обход графа в глубину (толкько связные графы)
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []
    stack = [node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node.key)
            result.append(node.key)
            for edge in node.edges:
                if edge.adjacent.key not in visited:
                    stack.append(edge.adjacent)

    return result


def dfs_wrapper(graph: Graph, helper: Callable = dfs) -> list[NodeKey]:
    """
    Обход графа в глубину.
    """
    visited = set()
    result = []

    # Одного прохода может быть недостаточно для обхода всего графа, если он несвязный
    for node in graph.nodes.values():
        if node.key not in visited:
            helper(node, visited, result)

    return result
