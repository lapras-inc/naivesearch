from typing import List, Protocol, Iterable


class Chunker(Protocol):
    def __call__(self, inputs: str) -> List[str]:
        ...


class Reader(Iterable[str]):
    pass
