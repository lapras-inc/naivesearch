from typing import Callable, List, Optional

from naivesearch.indexer import InvertedIndex
from naivesearch.preprocessors import UnicodeNormalizer, LowerCaseNormalizer
from naivesearch.preprocessors import BigramConverter
from naivesearch.preprocessors import CharacterChunker


class TestInvertedIndex:
    def test_getitem(self):
        def dummy_chunker(x):
            return list(x)

        def dummy_chunker2(x):
            return list(x.upper())

        data = [
            'hello world',
            'good bye world',
            'good morning world',
        ]

        index = InvertedIndex(
            # TODO: pycharm だと型が Reader じゃないと怒られる
            data,
            [
                dummy_chunker,
                dummy_chunker2,
            ],
        )

        assert 'hello world' in index['h']
        assert 'hello world' in index['H']
        assert 'hello world' in index['hello']

        assert 'hello world' not in index['へ']

        assert 'good bye world' in index['good b']
        assert 'good morning world' not in index['good b']

    def test_instantiate_composed_formatters(self):
        jinkou1 = '人口'
        jinkou2 = '⼈⼝'
        upper = 'UPPER'
        lower = 'upper'

        assert jinkou1 != jinkou2

        def reader():
            yield jinkou1
            yield upper
            yield 'hello world'
            yield 'good bye world'
            yield 'good morning world'

        index = InvertedIndex(
            reader(),
            [
                BigramConverter(CharacterChunker(
                    UnicodeNormalizer(LowerCaseNormalizer()),
                ))
            ]
        )

        assert jinkou1 in index[jinkou2]
        assert upper in index[lower]
