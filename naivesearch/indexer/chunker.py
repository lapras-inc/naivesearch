from typing import Callable, Protocol, List, Optional

from .formatter import Formatter


class Chunker(Protocol):
    def __init__(self, formatter: Optional[Formatter]):
        ...

    def __call__(self, x: str) -> List[str]:
        ...


class CharacterChunker:
    def __init__(self, formatter: Optional[Formatter]):
        self.formatter = formatter

    def __call__(self, x: str) -> List[str]:
        return list(self.formatter(x) if self.formatter else x)
