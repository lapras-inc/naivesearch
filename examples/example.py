from naivesearch import naivesearch


index = naivesearch('./examples/prefectures.txt')
print('`京`で検索', index['京'])
print()
print('`京都`で検索', index['京都'])
print()
print('`京都府`で検索', index['京都府'])
