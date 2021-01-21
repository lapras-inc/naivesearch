from typing import Callable, Protocol, List

Chunker = Callable[[str], List[str]]
