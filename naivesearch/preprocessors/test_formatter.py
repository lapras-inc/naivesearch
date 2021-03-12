from unittest.mock import Mock

from .formatter import UnicodeNormalizer, LowerCaseNormalizer


class TestFormatter:
    def test_unicode_normalizer(self):
        formatter = UnicodeNormalizer()
        lhs = '人口'
        rhs = '⼈⼝'
        assert lhs != rhs
        assert formatter(lhs) == formatter(rhs)

    def test_unicode_normalizer_instanciate_with_another_formatter(self):
        lhs = '人口'
        rhs = '⼈⼝'
        another = Mock(return_value='人口')
        formatter = UnicodeNormalizer(another)
        assert lhs != rhs
        assert formatter(lhs) == formatter(rhs)
        assert another.called

    def test_lower_case_normalizer(self):
        formatter = LowerCaseNormalizer()
        lhs = 'UPPER'
        rhs = 'upper'
        assert formatter(lhs) == formatter(rhs)

    def test_lower_case_normalizer_instanciate_with_another_formatter(self):
        lhs = 'UPPER'
        rhs = 'upper'
        another = Mock(return_value=lhs)
        formatter = LowerCaseNormalizer(another)
        assert formatter(lhs) == formatter(rhs)
        assert another.called
