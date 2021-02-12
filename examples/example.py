from naivesearch import naivesearch


index = naivesearch('./examples/prefectures.txt')
print('`京`で検索', index['京'])
print()
print('`京都`で検索', index['京都'])
print()
print('`京都府`で検索', index['京都府'])
print()

index_2 = naivesearch('./examples/fruits.txt')
print('`apple`で検索', index_2['apple'])  # Apple
print()
print('`APPLE`で検索', index_2['APPLE'])  # Apple
print()
print('`Orange`で検索', index_2['Orange'])  # Orange
print()
print('`ORANGE`で検索', index_2['ORANGE'])  # Orange
print()
print('`京都`で検索', index_2['京都'])  # ヒットしない
print()
