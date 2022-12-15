diary = {}
while True:
    information = input()
    if information == "END":
        break
    tokens = information.split("->")
    command = tokens[0]
    store = tokens[1]

    if command == "Add":
        item = tokens[2]
        if store in diary.keys():
            diary[store] += ("," + item)
        else:
            diary[store] = item
    elif command == "Remove":
        if store in diary.keys():
            del diary[store]

for key, value in diary.items():
    diary[key] = value.split(",")

# def sorted_by_values_len(notes):
#     notes_len = {key: len(value) for key, value in notes.items}
#     import operator
#     sorted_key_list = sorted(notes_len.items(), key=operator.itemgetter(1, reversed=True))
#     sorted_dict = [{item[0]: notes[item[0]]} for item in sorted_key_list]
#     return sorted_dict

print("Stores list:")
for key, value in diary.items():
    diary[key] = sorted(diary, key=lambda key: len(diary[key]), reverse=True)
    print(f"{key}")
    for item in value:
        print(f"<<{item}>>")
