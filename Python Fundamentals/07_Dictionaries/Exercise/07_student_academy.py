rows = int(input())
students = {}
filtered_students = {}

for i in range(rows):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(student_grade)

for key, value in students.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.50:
        filtered_students[key] = average_grade

# filtered_students = {key: sum(value) / len(value) for key, value in students.items() if sum(value) / len(value >= 4.50)}

sorted_students = dict(sorted(filtered_students.items(), key=lambda x: x[1], reverse=True))
for key, value in sorted_students.items():
    print(f"{key} -> {value:.2f}")
