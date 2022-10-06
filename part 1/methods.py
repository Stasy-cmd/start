from datetime import date
class User:
    count_ =0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_count(cls):
        cls.count_ += 1

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = User('Stasy', 29)
person2 = User.from_birth_year('Petr', 1995)

print(person1.name, person1.age)
print(person2.name, person2.age)
print(User.is_adult(25))

person2.change_count()
print(person1.count_)
