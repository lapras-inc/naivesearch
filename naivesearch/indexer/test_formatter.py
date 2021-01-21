from naivesearch import InvertedIndex
from typing import Callable, List, Optional
from .formatter import UnicodeNormalizer

class TestFormatter:
    def test_unicode_normalizer(self):

        formatter = UnicodeNormalizer()
        lhs = '人口'
        rhs = '⼈⼝'
        assert lhs != rhs
        assert formatter(lhs) == formatter(rhs)
