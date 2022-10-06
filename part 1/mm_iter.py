class Student:
    def __init__(self, name, course):
       self.name = name
       self.course = course
       self.param = []

       print('Start')

    def __repr__(self):
        return f"Student({self.name!r}, {self.course!r})"

    def __str__(self):
        return f"Student: {self.name}, {self.course}"

    def __iter__(self):
        self._room = [1, 1, 3]
        print("Создается итерабельный объект")
        return self

    def __next__(self):
        if self.param:
            return self.param.pop()
        else:
            raise StopIteration("Студентов в комнате нет")


student = Student("Stasy", "Python")
for i in student:
        print(f"{i}")
