class Student:
    def __init__(self, name, course):
       self.name = name
       self.course = course

    def __repr__(self):
        print('1')
        return f"Student:('{self.name}', '{self.course}')"


    # def __str__(self):
    #     print('2')
    #     return f"Student: {self.name}, {self.course}"

student = Student("Stasy", "Python")
# student.__repr__()
res = student
print(res)
# evaluated = eval(repr(student))
# print(type(evaluated))
# print(student)
# print(student.__repr__())
# print(student)