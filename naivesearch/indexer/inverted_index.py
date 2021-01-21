import logging

from collections import defaultdict
from typing import Dict, List, Protocol, Iterable
from .chunker import Chunker


logger = logging.getLogger(__name__)




class Reader(Iterable[str]):
    pass

class InvertedIndex:
    index: Dict[str, List[str]] = defaultdict(list)

    def __init__(self, reader: Reader, chunkers: List[Chunker]):
        logger.info('Start indexing.')
        for d in reader:
            for chunker in chunkers:
                for chunk in chunker(d):
                    self.index[chunk].append(d)
        logger.info('Done indexing.')

    def __getitem__(self, q):
        return self.index[q]
