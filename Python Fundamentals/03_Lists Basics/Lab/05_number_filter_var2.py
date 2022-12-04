n = int(input())

numbers = []

for i in range(n):
    number = int(input())
    numbers.append(number)

command = input()
filtered = []
for number in numbers:
    filter_passes = (
        (command == "even" and number % 2 == 0) or
        (command == "odd" and number % 2 != 0) or
        (command == "negative" and number < 0) or
        (command == "positive" and number >= 0)
    )
    if filter_passes:
        filtered.append(number)

print(filtered)
