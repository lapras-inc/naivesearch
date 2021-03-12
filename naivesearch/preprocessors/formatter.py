import unicodedata
from typing import Optional

from naivesearch.indexer import Formatter


class UnicodeNormalizer:
    def __init__(self, other: Optional[Formatter] = None, form: str = 'NFKC'):
        self.other = other
        self.form = form

    def __call__(self, x: str) -> str:
        x = self.other(x) if self.other else x
        return unicodedata.normalize(self.form, x)


class LowerCaseNormalizer:
    def __init__(self, other: Optional[Formatter] = None):
        self.other = other

    def __call__(self, x: str) -> str:
        x = self.other(x) if self.other else x
        return x.lower()
