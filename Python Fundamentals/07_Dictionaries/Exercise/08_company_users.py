companies = {}

while True:
    command = input()
    if command == "End":
        break

    company = command.split(" -> ")
    name = company[0]
    employee = company[1]
    if name not in companies:
        companies[name] = []
    if employee in companies[name]:
        continue

    companies[name].append(employee)
    sorted_companies = dict(sorted(companies.items(), key=lambda x: x[0]))

for key, value in sorted_companies.items():
    print(f"{key}")
    for i in value:
        print(f"-- {i}")
