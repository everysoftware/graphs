from dataclasses import dataclass

from src.models.types import NodeKey, Weight

EdgeData = tuple[NodeKey, NodeKey, Weight]


@dataclass
class GraphData:
    """
    Данные о графе для его создания.
    """

    size: int
    edges: list[EdgeData]

    def graphviz(self) -> str:
        """
        Возвращает строку с описанием графа в формате DOT.
        """
        graphviz = "digraph {\n"

        for edge in self.edges:
            graphviz += f"{edge[0]} -> {edge[1]} [label={edge[2]}];\n"

        graphviz += "}"

        return graphviz
