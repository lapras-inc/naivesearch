from naivesearch import InvertedIndex


class TestInvertedIndex:
    def test_getitem(self):
        def dummy_chunker(x):
            return list(x)

        index = InvertedIndex(
            '/path/to/hoge',
            [
                dummy_chunker,
            ],
        )

        assert 'hoge' in index['ho']
        assert 'hoo' in index['ho']
        assert 'foo' not in index['ho']
