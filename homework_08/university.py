from student import Student

students = [Student('Polina', 8),
            Student('Kolya', 9),
            Student('Liza', 7),
            Student('Sasha', 6)]


def calc_sum_scholarship(lst: list):
    summ = 0
    for student in lst:
        summ += student.get_scholarship()
    return summ


def get_exellent_student_count(lst: list):
    count = 0
    for student in lst:
        if student.is_excellent():
            count += 1
    return count


print(f"The summ scholarship: {calc_sum_scholarship(students)}")


print(f"Exellent student count: {get_exellent_student_count(students)}")


