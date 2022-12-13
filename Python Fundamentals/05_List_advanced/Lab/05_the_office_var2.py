employee_happiness = list(map(int, input().split()))
factor = int(input())
new_list = list(map(lambda n: n * factor, employee_happiness))
new_list_average_sum = (sum(new_list)) / len(new_list)
happy_employee = list(filter(lambda n: n >= new_list_average_sum, new_list))

if len(happy_employee) >= len(employee_happiness) / 2:
    print(f"Score: {len(happy_employee)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employee)}/{len(employee_happiness)}. Employees are not happy!")