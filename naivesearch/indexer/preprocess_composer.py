from typing import Callable, List, Optional, Protocol, Type


class Formatter(Protocol):
    def __init__(self, other: Optional['Formatter'] = None, **kwargs):
        ...

    def __call__(self, x: str) -> str:
        ...


class Chunker(Protocol):
    def __init__(self, formatter: Optional[Formatter]):
        ...

    def __call__(self, x: str) -> List[str]:
        ...


class Converter(Protocol):
    def __init__(self, chunker: Chunker):
        ...

    def __call__(self, x: str) -> List[str]:
        ...


def compose_preprocessors(
        converter: Type[Converter],
        chunker: Type[Chunker],
        *formatters: Callable[..., Formatter],
) -> Converter:
    result = None
    for x in reversed(formatters):
        result = x(result)
    return converter(chunker(result))
