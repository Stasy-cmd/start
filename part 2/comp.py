numbers = [1, 2, 3, 4, 5]
squared_numbers = {x:x*x for x in numbers}
print(squared_numbers)

squared_numbers = []
for x in numbers:
    squared_numbers.append(x*x)
print(squared_numbers)


seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)
seq2 = (5, 6, 7, 8, 9, 0, 3, 2, 1)
result = (x + y for x, y in zip(seq, seq2))
print(next(result))