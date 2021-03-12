from returns.curry import partial

from naivesearch.indexer import compose_preprocessors, InvertedIndex
from naivesearch.preprocessors import UnicodeNormalizer, LowerCaseNormalizer
from naivesearch.preprocessors import BigramConverter
from naivesearch.preprocessors import CharacterChunker


def naivesearch(filepath: str):
    index = InvertedIndex(
        file_reader(filepath),
        [
            compose_preprocessors(
                BigramConverter,
                CharacterChunker,
                LowerCaseNormalizer,
                partial(UnicodeNormalizer, form='NFKC'),
            )
        ]
    )
    return index


def file_reader(filepath):
    with open(filepath) as f:
        for line in f.readlines():
            yield line.strip()
