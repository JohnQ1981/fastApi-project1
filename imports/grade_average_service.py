def calculate_homework(homework_ass_arg):
    sum_of_grades = 0
    for homework in homework_ass_arg.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades / len(homework_ass_arg), 2)
    print(final_grade)