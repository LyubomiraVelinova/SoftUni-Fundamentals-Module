list_of_commands = [0] * 10

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split("-")
    index = int(tokens[0])
    task = tokens[1]
    list_of_commands.insert(index, task)

# list_of_commands_without_zeros = list_of_commands

new_list = [i for i in list_of_commands if i != 0]
# while 0 in list_of_commands:
#     list_of_commands.remove(0)
# print(list_of_commands_without_zeros)

print(new_list)
