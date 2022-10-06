import random

name_lengths = map(len, ['Настя', 'Петя', 'Ян'])
print(list(name_lengths))

squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
# print(next(squares))



names = ['Маша', 'Петя', 'Вася']
code_names = ['Шпунтик', 'Винтик', 'Фунтик']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print(names)

names = ['Маша', 'Петя', 'Вася']
secret_names = map(lambda x: random.choice(['Шпунтик', 'Винтик', 'Фунтик']), names)

print(list(secret_names))