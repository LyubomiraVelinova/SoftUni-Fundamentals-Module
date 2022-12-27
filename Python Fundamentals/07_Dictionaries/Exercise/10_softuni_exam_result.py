from collections import defaultdict

total = defaultdict(list)
languages_submissions = defaultdict(int)
username_points = defaultdict(int)
while True:
    line_input = input()
    if line_input == "exam finished":
        break
    if "-banned" in line_input:
        banned_username = line_input.split("-")[0]
        total.pop(banned_username)
    else:
        username, language_points = line_input.split("-", 1)
        language = language_points.split("-")[0]
        points = int(language_points.split("-")[1])
        if username in total.keys() and language in total[username]:
            if points > int(total[username][1]):
                total[username] = language_points.split("-")
        else:
            total[username] = language_points.split("-")
        languages_submissions[language] += 1

for key, value in total.items():
    username_points[key] += int(value[1])

ordered_by_points = dict(sorted(username_points.items(), key=lambda x: (-x[1], x[0])))
print("Results:")
for person in ordered_by_points:
    print(f"{person} | {int(ordered_by_points[person])}")
ordered_language_submissions = dict(sorted(languages_submissions.items(), key=lambda x: (-x[1], x[0])))
print(f"Submissions:")
for l in ordered_language_submissions.keys():
    print(f"{l} – {ordered_language_submissions[l]}")

