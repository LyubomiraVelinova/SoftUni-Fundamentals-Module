people = int(input())
capacity = int(input())

people_left = people % capacity

if people % capacity == 0:
    full_course = people // capacity
else:
    full_course = people // capacity + 1

print(f"{full_course}")
