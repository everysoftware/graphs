from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.node import Node
    from src.models.types import Weight


@dataclass
class Edge:
    """
    Ребро графа.
    """

    adjacent: Node
    """Узел, на который ведёт ребро."""
    weight: Weight
    """Вес ребра."""
