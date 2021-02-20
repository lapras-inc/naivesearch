from typing import Callable, Protocol, List

from .formatter import Formatter


Chunker = Callable[[str], List[str]]


class CharacterChunker:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter

    def __call__(self, x: str) -> List[str]:
        return list(self.formatter(x))
