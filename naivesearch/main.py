from returns.curry import partial
from typing import Callable, Type

from naivesearch.indexer import InvertedIndex
from naivesearch.indexer.formatter import UnicodeNormalizer, LowerCaseNormalizer, Formatter
from naivesearch.indexer.converter import BigramConverter
from naivesearch.indexer.chunker import CharacterChunker, Chunker


def naivesearch(filepath: str):
    index = InvertedIndex(
        file_reader(filepath),
        [
            composed(
                BigramConverter,
                CharacterChunker,
                LowerCaseNormalizer,
                partial(UnicodeNormalizer, form='NFKC'),
            )
        ]
    )
    return index


def composed(
        converter: Type[BigramConverter],
        chunker: Type[Chunker],
        *formatters: Callable[..., Formatter],
):
    result = None
    for x in reversed(formatters):
        result = x(result)
    return converter(chunker(result))


def file_reader(filepath):
    with open(filepath) as f:
        for line in f.readlines():
            yield line.strip()
