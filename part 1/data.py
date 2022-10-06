from dataclasses import dataclass


@dataclass      #(frozen=True)
class Student:
    name: str
    course: str
    age: int


student_1 = Student("Stasy", 'Python', 21)
print(student_1)

student_2 = Student("Stasy", 'Python', 21)
print(student_2.name)

print(student_2 == student_1)
student_2.name = 'New'
print(student_2)