from naivesearch import InvertedIndex
from typing import Callable, List, Optional

from .chunker import CharacterChunker
from .formatter import UnicodeNormalizer


class TestCharacterChunker:
    def test(self):
        format_chunker = CharacterChunker(UnicodeNormalizer())
        result = format_chunker('hello')
        assert result == ['h', 'e', 'l', 'l', 'o']
