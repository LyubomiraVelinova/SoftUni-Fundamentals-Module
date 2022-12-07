presents = input().split(" ")
command = input()

index = 0
list_of_command = []

while command != "No Money":
    list_of_command = command.split(" ")
    corrected_list = []
    if "OutOfStock" in command:
        for every_present in presents:
            if every_present in command:
                every_present = "None"
                corrected_list.append(every_present)
            else:
                corrected_list.append(every_present)
        presents = corrected_list
    elif "Required" in command:
        index = int(list_of_command[-1])
        if 0 <= index <= len(presents) - 1:
            presents[index] = list_of_command[1]
    elif "JustInCase" in command:
        presents[-1] = list_of_command[1]

    command = input()
    list_of_command = []

while "None" in presents:
    presents.remove("None")

print(" ".join(presents))