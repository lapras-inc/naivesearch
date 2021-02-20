from naivesearch.indexer import InvertedIndex
from naivesearch.indexer.formatter import UnicodeNormalizer, LowerCaseNormalizer
from naivesearch.indexer.converter import BigramConverter
from naivesearch.indexer.chunker import CharacterChunker


def naivesearch(filepath: str):

    def file_reader(filepath):
        with open(filepath) as f:
            for line in f.readlines():
                yield line.strip()

    index = InvertedIndex(
        file_reader(filepath),
        [
            BigramConverter(CharacterChunker(
                UnicodeNormalizer(LowerCaseNormalizer()),
            ))
        ]
    )
    return index
