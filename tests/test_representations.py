import pytest

from src.models.data import GraphData, EdgeData
from src.models.simple import (
    AdjacencyMatrix,
    AdjacencyList,
    edge_list,
    adjacency_matrix,
    adjacency_list,
)
from .data import graph_data


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            graph_data["short"],
            [
                (1, 2, 3),
                (1, 3, 11),
                (2, 3, 7),
            ],
        ),
        (
            graph_data["long"],
            [
                (1, 2, 7),
                (2, 5, 3),
                (3, 2, 4),
                (4, 4, 0),
                (5, 4, 1),
                (7, 1, 5),
            ],
        ),
    ],
)
def test_edge_list(data: GraphData, expected: list[EdgeData]):
    assert edge_list(data) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            graph_data["short"],
            [
                [0, 3, 11],
                [0, 0, 7],
                [0, 0, 0],
            ],
        ),
        (
            graph_data["long"],
            [
                [0, 7, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 3, 0, 0],
                [0, 4, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [5, 0, 0, 0, 0, 0, 0],
            ],
        ),
    ],
)
def test_adjacency_matrix(data: GraphData, expected: AdjacencyMatrix):
    result = adjacency_matrix(data)
    assert result == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            graph_data["short"],
            {
                1: [(2, 3), (3, 11)],
                2: [(3, 7)],
            },
        ),
        (
            graph_data["long"],
            {
                1: [(2, 7)],
                2: [(5, 3)],
                3: [(2, 4)],
                4: [(4, 0)],
                5: [(4, 1)],
                7: [(1, 5)],
            },
        ),
    ],
)
def test_adjacency_list(data: GraphData, expected: AdjacencyList):
    assert adjacency_list(data) == expected
