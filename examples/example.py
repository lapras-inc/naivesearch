# index = InvertedIndex(
#     '/path/to/file', # FileReader('/path/to/file')
#     [
#         compose(
#             UnicodeNormalizer(),
#             CharacterChunker(), # hello => h e l l o
#             NgramConverter([2, 3]) # h e l l o => he el ll lo
#         )
#         compose( # => heelo => h e l l o
#             UnicodeNormalizer(),
#             RubyFormater()
#             CharacterChunker(), # hello => h e l l o
#             NgramConverter([2, 3]) # h e l l o => he el ll lo
#         )
#     ]
# )

def split_sentence(s):
    return list(s)


class InvertedIndex:
    def __init__(self, path_to_file, chunkers):
        pass

    def __getitem__(self, q):
        return ['hoge', 'hoo']


index = InvertedIndex(
    '/path/to/file', # FileReader('/path/to/file')
    [
        split_sentence
    ]
)

print(index['ho']) #=> [hoge, hooo]
