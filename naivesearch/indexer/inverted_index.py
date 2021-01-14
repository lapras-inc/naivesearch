from typing import List

from .types import Chunker


class InvertedIndex:
    def __init__(self, path_to_file: str, chunkers: List[Chunker]):
        pass

    def __getitem__(self, q):
        return ['hoge', 'hoo']
