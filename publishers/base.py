from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class PublishResult:
    success: bool
    url: str = ""
    error: str = ""


class Publisher(ABC):
    name: str = "base"

    @abstractmethod
    def publish(self, article, image_path: Optional[str] = None) -> PublishResult:
        ...
