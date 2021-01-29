from naivesearch import InvertedIndex
from typing import Callable, List, Optional


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

