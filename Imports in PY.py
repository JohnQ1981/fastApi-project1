"""
Modules get used all the time throughout programming
"""
import imports.grade_average_service as grade_service
homework_ass_grades = {
    "homework1": 85,
    "homework2": 100,
    "homework3": 81,
    "homework4": 100
}

# def calculate_homework(homework_ass_arg):
#     sum_of_grades = 0
#     for homework in homework_ass_arg.values():
#         sum_of_grades += homework
#     final_grade = round(sum_of_grades / len(homework_ass_arg), 2)
#     print(final_grade)

grade_service.calculate_homework(homework_ass_grades)
#calculate_homework(homework_ass_grades)