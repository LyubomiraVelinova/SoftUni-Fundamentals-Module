bakery = {}

while True:
    command = input()
    if command == "statistics":
        break
    products = command.split(": ")
    product = products[0]
    quantity = int(products[1])
    if product not in bakery:
        bakery[product] = 0

    bakery[product] += quantity

print("Products in stock:")

for key, value in bakery.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")
