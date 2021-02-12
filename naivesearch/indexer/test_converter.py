from naivesearch import InvertedIndex
from typing import Callable, List, Optional

from .converter import BigramConverter
from .formatter import UnicodeNormalizer


class TestBigramConverter:
    def test(self):
        def dummy_chunker(x):
            return list(x)

        convert_chunker = BigramConverter(dummy_chunker)
        result = convert_chunker('hello')
        assert result == ['he', 'el', 'll', 'lo']

    def test(self):
        def dummy_chunker(x):
            return list(x)

        convert_chunker = BigramConverter(dummy_chunker)
        result = convert_chunker('hello')
        assert result == [
            'h', 'e', 'l', 'l', 'o',
            'he', 'el', 'll', 'lo'
        ]
