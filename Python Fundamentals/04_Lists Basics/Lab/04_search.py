n = int(input())
word = input()

list_of_strings = []
filtered_list = []

for i in range(n):
    current_string = input()
    list_of_strings.append(current_string)

    if word in current_string:
        filtered_list.append(current_string)

print(list_of_strings)
print(filtered_list)