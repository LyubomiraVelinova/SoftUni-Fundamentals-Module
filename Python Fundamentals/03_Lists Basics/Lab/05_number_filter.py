n = int(input())

list_of_numbers = []
filtered_list = []

for i in range(n):
    current_number = int(input())
    list_of_numbers.append(current_number)

command = input()

for every_num in list_of_numbers:
    if command == "even" and every_num % 2 == 0:
        filtered_list.append(every_num)
    elif command == "odd" and every_num % 2 != 0:
        filtered_list.append(every_num)
    elif command == "positive" and every_num >= 0:
        filtered_list.append(every_num)
    elif command == "negative" and every_num < 0:
        filtered_list.append(every_num)

print(filtered_list)