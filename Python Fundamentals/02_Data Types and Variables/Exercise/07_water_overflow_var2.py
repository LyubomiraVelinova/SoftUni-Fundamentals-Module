n = int(input())
CAPACITY = 255

total_liters = 0
for i in range(n):
   liters = int(input())
   if total_liters + liters > CAPACITY:
        print("Insufficient capacity!")
   else:
        total_liters +=liters

print(total_liters)