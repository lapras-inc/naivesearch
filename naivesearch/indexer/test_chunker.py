from naivesearch import InvertedIndex
from typing import Callable, List, Optional

from .chunker import CharacterChunker
from .formatter import LowerCaseNormalizer, UnicodeNormalizer


class TestCharacterChunker:
    def test(self):
        format_chunker = CharacterChunker(
            UnicodeNormalizer(LowerCaseNormalizer()),
        )
        result = format_chunker('Hello')
        assert result == ['h', 'e', 'l', 'l', 'o']
