n_lines = int(input())

student_grades = {}

for _ in range(n_lines):
    name, grade = input().split()

    if name not in student_grades:
        student_grades[name] = []

    student_grades[name].append(float(grade))

for student, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    all_grades = ' '.join(f'{grade:.2f}' for grade in grades)

    print(f'{student} -> {all_grades} (avg: {average_grade:.2f})')
