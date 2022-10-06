class Student_:
   def __init__(self, name, course):
       self.name = name
       self.course = course


print(Student_("Stasy", 'Python'))
print('________')

class Student:

    def __new__(cls, *args):
        new_student = object.__new__(cls)
        #print("Student __new__ gets called")
        return new_student

    def __init__(self, name, course):
        self.name = name
        # self.course = course
        print("Student __init__ gets called")

class Room:
    student_lst = []

    def __new__(cls, *args):
        if cls.student_lst:
            return 'Error'
        else:
            cls.student_lst.append(Student("Stasy", 'Python'))
            return object.__new__(cls)



room = Room()
print(Room())
print(room.student_lst)
#print(Student("Petr", 'Python'))