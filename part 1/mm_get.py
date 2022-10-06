class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    # def __getattr__(self, item):
    #     return 'Nothing found.'

    def __getattribute__(self, item):
    #     # if item not in ['name', 'course']: #if item not in self.__dict__:
    #     #     return 'nope attr'
    #     # if item.startswith('name'):
    #     #     raise AttributeError
         return object.__getattribute__(self, item) # или вы можете использовать return super().__getattribute__(item)

obj1 = Student("Petr", 'Python')
print(obj1.name)  # Petr
print(obj1.course)  # Python
print(obj1.current) # nope attr