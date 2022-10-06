x = 'абв'
y = 'эюя'
zipped = zip(x, y)
print(list(zipped))

x2, y2 = zip(*zip(x, y))
print(x2)
print(y2)

print(x == ''.join(x2) and y == ''.join(y2))

lazy = enumerate(['а','б','в'])
print(list(lazy))