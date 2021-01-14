from typing import List, Protocol


class Chunker(Protocol):
    def __call__(self, inputs: str) -> List[str]:
        ...
