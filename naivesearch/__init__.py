from typing import List, Optional, Protocol

class Chunker(Protocol):
    def __call__(self, inputs: str) -> List[str]:
        ...


class InvertedIndex:
    def __init__(self, path_to_file: str, chunkers: List[Chunker]):
        pass

    def __getitem__(self, q):
        return ['hoge', 'hoo']


