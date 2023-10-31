
class Student:
    pass

student_1 = Student()
student_2 = Student()

student_1.first_name = "Eric"
student_1.last_name = "Roby"
student_1.major = "Computer Science"

student_2.first_name = "John"
student_2.last_name = "Qo"
student_2.major = "Math"

print(student_1.first_name, student_1.last_name, student_1.major)
print(student_2.first_name)

class Students:
    def __init__(self, firstn, lastn, major):
        self.firstn = firstn
        self.lastn = lastn
        self.major = major

students001 = Students("Salih", "Kuch", "Marine")
print(students001.firstn, students001.major)
