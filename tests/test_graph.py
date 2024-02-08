import pytest

from src.controllers.graph import Graph
from src.models.types import NodeKey
from .data import graphs


@pytest.mark.parametrize(
    "graph, expected",
    [
        (graphs["short"], [1, 2, 3]),
        (graphs["long"], [1, 2, 5, 4, 3, 7]),
    ],
)
def test_dfs(graph: Graph, expected: list[NodeKey]):
    result = graph.dfs()
    assert result == expected


@pytest.mark.parametrize(
    "graph, expected",
    [
        (graphs["short"], [1, 3, 2]),
        (
            graphs["long"],
            [1, 2, 5, 4, 3, 7],
        ),
    ],
)
def test_dfs_iterative(graph: Graph, expected: list[NodeKey]):
    result = graph.dfs_iterative()
    assert result == expected


@pytest.mark.parametrize(
    "graph, expected",
    [
        (graphs["short"], [1, 2, 3]),
        (
            graphs["long"],
            [1, 2, 5, 4, 3, 7],
        ),
    ],
)
def test_bfs(graph: Graph, expected: list[NodeKey]):
    result = graph.bfs()
    assert result == expected


@pytest.mark.parametrize(
    "graph, start, end, expected",
    [
        (graphs["short"], 1, 3, [1, 2, 3]),
        (graphs["short"], 2, 1, []),
    ],
)
def test_find_path(graph: Graph, start: NodeKey, end: NodeKey, expected: list[NodeKey]):
    result = graph.find_path(graph.get(start), graph.get(end))
    assert result == expected


@pytest.mark.parametrize(
    "graph, start, end, expected",
    [
        (graphs["short"], 1, 3, [[1, 2, 3], [1, 3]]),
        (graphs["short"], 2, 1, []),
    ],
)
def test_find_path_all(
    graph: Graph, start: NodeKey, end: NodeKey, expected: list[list[NodeKey]]
):
    result = graph.find_path_all(graph.get(start), graph.get(end))
    assert result == expected


@pytest.mark.parametrize(
    "graph, start, end, expected",
    [
        (graphs["short"], 1, 3, [1, 3]),
        (graphs["short"], 2, 1, []),
    ],
)
def test_find_shortest_path(
    graph: Graph, start: NodeKey, end: NodeKey, expected: list[list[NodeKey]]
):
    result = graph.find_shortest_path(graph.get(start), graph.get(end))
    assert result == expected


@pytest.mark.parametrize(
    "graph, start, end, expected",
    [
        (graphs["short"], 1, 3, [1, 2, 3]),
        (graphs["short"], 2, 1, []),
        (graphs["long2"], 1, 6, [1, 3, 5, 6]),
    ],
)
def test_dijkstra(graph: Graph, start: NodeKey, end: NodeKey, expected: list[NodeKey]):
    result = graph.dijkstra(graph.get(start), graph.get(end))
    assert result == expected

    result_heap = graph.dijkstra_heap(graph.get(start), graph.get(end))
    assert result_heap == expected
