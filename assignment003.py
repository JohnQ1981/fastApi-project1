"""- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable
Grades:

A = 90 - 100

B = 80 - 89

C = 70-79

D = 60 - 69

F = 0 - 59

Example:

if grade = 87 then print('B')
"""
grade = int(input("Enter Your Score between 0 and 100 "))
if grade == 0 or grade < 60:
    print(f"You got F since your grade is {grade}")
elif grade == 60 or grade < 70:
    print(f"You got D since your grade is {grade}")
elif grade == 70 or grade < 80:
    print(f"You got C since your grade is {grade}")
elif grade == 80 or grade < 89:
    print(f"You got B since your grade is {grade}")
else: 
    print(f"You got A since your grade is {grade}")

print("enter one more time")
grade = int(input("Enter Your Score between 0 and 100 "))
if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60<= grade < 70 :
    print("D")
else:
    print("F")