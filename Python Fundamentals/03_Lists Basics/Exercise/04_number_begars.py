nums_str = input().split(", ")
beggars_count = int(input())

numbers = []
for every_num in nums_str:
    numbers.append(int(every_num))

beggars = []
for i in range(beggars_count):
    beggars.append(0)

index = 0
for number in numbers:
    beggars[index] += number
    index += 1

    if index == beggars_count:
        index = 0

print(beggars)