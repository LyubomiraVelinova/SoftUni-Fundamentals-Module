first_line = input().split()
food = {}
for i in range(0, len(first_line) + 1, 2):
    food[first_line[i]] = first_line[i + 1]

print(food)
