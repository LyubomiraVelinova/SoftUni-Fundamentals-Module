text = input()

list_of_capitals = []
count = 0

for every_letter in text:
    if 65 <= ord(every_letter) <= 90:
        list_of_capitals.append(count)
    count +=1

print(list_of_capitals)