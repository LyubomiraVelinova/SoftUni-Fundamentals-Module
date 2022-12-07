import sys

numbers = input().split(" ")
n = int(input())

list_of_left_nums = []
for j in numbers:
    list_of_left_nums.append(int(j))

for i in range(n):
    smallest_num = sys.maxsize
    for every_num in list_of_left_nums:
        if every_num < smallest_num:
            smallest_num = every_num
    list_of_left_nums.remove(smallest_num)

print(list_of_left_nums)