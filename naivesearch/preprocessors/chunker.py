from typing import List, Optional

from naivesearch.indexer import Formatter


class CharacterChunker:
    def __init__(self, formatter: Optional[Formatter]):
        self.formatter = formatter

    def __call__(self, x: str) -> List[str]:
        return list(self.formatter(x) if self.formatter else x)
