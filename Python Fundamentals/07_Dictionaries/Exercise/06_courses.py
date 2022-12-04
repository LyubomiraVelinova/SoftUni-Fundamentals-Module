line = input()
courses = {}

while line != "end":
    command = line.split(" : ")
    course_name = command[0]
    student_name = command[1]

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)
    line = input()

sorted_courses = dict(sorted(courses.items(), key=lambda c: len(c[1]), reverse=True))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")

    for i in sorted(value):
        print(f"-- {i}")
