
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

    school = "Online School"
    number_of_students = 0

    def __init__(self, firstn, lastn, major):
        self.firstn = firstn
        self.lastn = lastn
        self.major = major

        Students.number_of_students +=1
    
    def fullname_with_major(self):
        return f'{self.firstn} {self.lastn} is a '\
        f'{self.major} major!'
    
    def fullname_major_school(self):
        return f'{self.firstn} {self.lastn} is a ' \
               f'{self.major} going to {self.school} !.'


print(f'Number of Students = {Students.number_of_students}')
students001 = Students("Salih", "Kuch", "Marine")
students002 = Students("Zayd", "Kuch", "Dentist")
students003 = Students("Ihsan", "Kuch", "Math")
print(students001.firstn, students001.major)
print(students002.firstn, students002.lastn, students002.major)

print(students001.fullname_with_major())
print(students002.fullname_with_major())
print("-------------")
print(Students.fullname_with_major(students002))
print("-------------")
print(students001.school)
print("-------------")
print(Students.fullname_major_school(students001))
print(Students.fullname_major_school(students003))
print("-------------")
print(f'Number of Students = {Students.number_of_students}')


