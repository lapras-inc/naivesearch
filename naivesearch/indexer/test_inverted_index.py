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

        # sample desu
        Formatter = Callable[[str], str]

        class UpperCaseFormatter:
            def __call__(self, x: str) -> str:
                return x.upper()

        class CharacterChunker:
            def __init__(self, formatter: Optional[Formatter]):
                self.formatter = formatter
            def __call__(self, x: str) -> List[str]:
                return list(self.formatter(x) if self.formatter else x)

        chunker = CharacterChunker(UpperCaseFormatter())
        assert chunker('heelo') == ['H', 'E', 'E', 'L', 'O']
