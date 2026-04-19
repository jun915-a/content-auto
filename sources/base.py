from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class TrendItem:
    title: str
    url: str
    source: str
    score: int = 0
    description: str = ""


class TrendSource(ABC):
    name: str = "base"

    @abstractmethod
    def fetch(self, limit: int = 10) -> List[TrendItem]:
        ...
