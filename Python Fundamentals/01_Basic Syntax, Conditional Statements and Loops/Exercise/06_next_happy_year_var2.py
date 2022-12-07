year = int(input())

while year > 0:
    year += 1

    year_to_str = str(year)
    year_to_set = set(year_to_str)
    if len(year_to_str) == len(year_to_set):
        break

print(year)