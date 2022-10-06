from functools import reduce

sum = reduce(lambda a, x: a * x, [1, 2, 3, 4], 0)
# x – текущий пункт, а – аккумулятор
# Первая итерация - первый элемент коллекции
# Reduce() начинает работать со второго элемента. Первый х - второй предмет набора.
print (sum)

sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

a = 0
for sentence in sentences:
    a += sentence.count('капитан')

print(a)

sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = reduce(lambda a, x: a + str(x.count('капитан')),
                   sentences)
print(cap_count)