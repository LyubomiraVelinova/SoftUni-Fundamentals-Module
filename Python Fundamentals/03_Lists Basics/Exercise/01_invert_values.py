string = input()
list_of_string = string.split(" ")

new_list = []

for every_string in list_of_string:
    number = - int(every_string)
    new_list.append(number)

print(new_list)