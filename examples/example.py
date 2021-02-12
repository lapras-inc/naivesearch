import os

from naivesearch.indexer import InvertedIndex
from naivesearch.indexer.formatter import UnicodeNormalizer
from naivesearch.indexer.converter import BigramConverter
from naivesearch.indexer.chunker import CharacterChunker

with open(os.path.join(os.path.dirname(__file__), './prefectures.txt')) as f:
    prefectures = []
    for line in f.readlines():
        prefectures.append(line.strip())

def prefecture_reader():
    for x in prefectures:
        yield x

index = InvertedIndex(
    prefecture_reader(),
    [
        BigramConverter(CharacterChunker(UnicodeNormalizer()))
    ]
)

print('これです', index['京都'])
