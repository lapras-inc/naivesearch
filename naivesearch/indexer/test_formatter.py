from naivesearch import InvertedIndex
from typing import Callable, List, Optional
from .formatter import UnicodeNormalizer, LowerCaseNormalizer


class TestFormatter:
    def test_unicode_normalizer(self):

        formatter = UnicodeNormalizer()
        lhs = '人口'
        rhs = '⼈⼝'
        assert lhs != rhs
        assert formatter(lhs) == formatter(rhs)

    def test_lower_case_normalizer(self):
        formatter = LowerCaseNormalizer()
        lhs = 'UPPER'
        rhs = 'upper'
        assert formatter(lhs) == formatter(rhs)
