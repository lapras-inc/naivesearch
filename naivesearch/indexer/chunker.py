from typing import Callable, Protocol, List

from .formatter import Formatter

Chunker = Callable[[str], List[str]]


class CharacterChunker:
    def __init__(self, formatters: List[Formatter]):
        self.formatters = formatters

    def __call__(self, x: str) -> List[str]:
        for formatter in self.formatters:
            x = formatter(x)
        return list(x)
