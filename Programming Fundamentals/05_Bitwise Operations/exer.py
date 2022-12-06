num_1 = int(input())
num_2 = int(input())

result = num_1
binary_list = []
while result != 0:
    residue = result % 2
    result = result // 2

    binary_list.append(residue)

counter = 0
for i in range(len(binary_list)-1,-1,-1):
    if binary_list[i] == num_2:
        counter += 1

print(counter)