import random

#Глобальной мутация
def append_one(xs):
    xs.append(1)
    return xs

xs = []
print(append_one(xs))
print(append_one(xs))

#Недетерминированности:
print(random.random())
print(random.random())

#Ввода - вывода:
with open('temp.txt', 'w')as f:
    f.write('Hello!')

with open('temp.txt', 'r')as f:
    print(f.read ())

with open('temp.txt', 'w')as f:
    f.write('Hi!')

with open('temp.txt', 'r')as f:
    print(f.read ()) 