import unicodedata
from typing import Callable, Optional

Formatter = Callable[[str], str]


class UnicodeNormalizer:
    def __init__(self, other: Optional[Formatter] = None):
        self.other = other

    def __call__(self, x: str):
        x = self.other(x) if self.other else x
        return unicodedata.normalize('NFKC', x)


class LowerCaseNormalizer:
    def __init__(self, other: Optional[Formatter] = None):
        self.other = other

    def __call__(self, x: str):
        x = self.other(x) if self.other else x
        return x.lower()
