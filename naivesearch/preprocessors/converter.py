from typing import List

from naivesearch.indexer import Chunker


class BigramConverter:
    def __init__(self, chunker: Chunker):
        self.chuker = chunker

    def __call__(self, x: str) -> List[str]:
        s = self.chuker(x)
        return s + [''.join(z) for z in zip(s[0:], s[1:])]
