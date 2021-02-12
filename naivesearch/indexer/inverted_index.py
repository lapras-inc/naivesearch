import logging

from collections import defaultdict
from typing import Dict, List, Protocol, Iterable
from .chunker import Chunker


logger = logging.getLogger(__name__)


class Reader(Iterable[str]):
    pass


class InvertedIndex:
    chunkers: List[Chunker]

    def __init__(self, reader: Reader, chunkers: List[Chunker]):
        self.index: Dict[str, List[str]] = defaultdict(list)
        self.chunkers = chunkers

        logger.info('Start indexing.')
        for d in reader:
            for chunker in chunkers:
                for chunk in chunker(d):
                    self.index[chunk].append(d)
        logger.info('Done indexing.')

    def __getitem__(self, q):
        chunks = []
        for chunker in self.chunkers:
            for chunk in chunker(q):
                chunks.append(chunk)

        # Chunkごとにindexにヒットした短文のsetのリスト
        chains = [set(self.index[chunk]) for chunk in chunks]

        # すべてのChunkでindexにヒットした候補を結果として返す
        result = chains[0]
        for chain in chains:
            result = result & chain

        return list(result)
