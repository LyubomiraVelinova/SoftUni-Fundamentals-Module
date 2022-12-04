line = input()
orders = {}
name_quantity = {}
total = 0

while line != "buy":
    command = line.split()
    name = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if name not in orders:
        orders[name] = price
        name_quantity[name] = quantity
    else:
        name_quantity[name] += quantity
        if orders.values() != price:
            orders[name] = price
    line = input()

for name, price in orders.items():
    total = name_quantity[name] * orders[name]
    print(f"{name} -> {total:.2f}")
