import unicodedata
from typing import Callable

Formatter = Callable[[str], str]


class UnicodeNormalizer:
    def __call__(self, x: str):
        return unicodedata.normalize('NFKC', x)


class LowerCaseNormalizer:
    def __call__(self, x: str):
        return x.lower()
