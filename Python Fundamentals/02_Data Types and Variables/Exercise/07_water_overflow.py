CAPACITY = 255
n = int(input())

liters_in_tank = 0

for i in range(n):
    water_quantity = int(input())
    if liters_in_tank <= CAPACITY:
        liters_in_tank += water_quantity
    if liters_in_tank > CAPACITY:
        liters_in_tank -= water_quantity
        print(f"Insufficient CAPACITY!")
print(f"{liters_in_tank}")