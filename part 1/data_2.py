from dataclasses import dataclass, field


@dataclass      #(frozen=True)
class Student:

    course: str
    age: int
    count = 1
    first: str = '111'
    #books: list[int] = [] #mutable default <class 'list'> for field books is not allowed: use default_factory
    #books: list[int] = field()
    @classmethod
    def start(cls):
        cls.count += 1


student_1 = Student([1, 2, 3], 'Python')
student_1.start()
print(student_1)

# student_2 = Student("Stasy", 'Python', 21)
# print(student_2.name)
#
# print(student_2 == student_1)
# student_2.name = 'New'
# print(student_2)