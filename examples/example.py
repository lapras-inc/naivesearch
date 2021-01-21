

# index = InvertedIndex(
#     '/path/to/file', # FileReader('/path/to/file')
#     [
#         UnicodeNormalizer: str -> str # formater
#         CharacterChunker: str -> List[str] # chunker
#         NgramConverter: List[str] -> List[str] # converter

#         NgramConverter(CharacterChunker(UnicodeNormalizer()), ngrams=[2, 3]),
#         CharacterChunker(UnicodeNormalizer())),
#     ]
#     # [
#     #     compose(
#     #         UnicodeNormalizer(),
#     #         CharacterChunker(), # hello => h e l l o
#     #         NgramConverter([2, 3]) # h e l l o => he el ll lo
#     #     )
#     #     compose( # => heelo => h e l l o
#     #         UnicodeNormalizer(),
#     #         RubyFormater()
#     #         CharacterChunker(), # hello => h e l l o
#     #         NgramConverter([2, 3]) # h e l l o => he el ll lo
#     #     )
#     # ]
# )
