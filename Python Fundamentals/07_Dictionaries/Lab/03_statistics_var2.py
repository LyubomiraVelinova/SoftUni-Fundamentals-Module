from collections import defaultdict

bakery = defaultdict(int)
while True:
    line_input = input()
    if line_input == "statistics":
        break
    product, quantity = line_input.split()
    bakery[product] += int(quantity)

print("Products in stock:")
for product_name, value in bakery.items():
    print(f"- {product_name}: {value}")

print(f"Total Products: {len(bakery.keys())}\nTotal Quantity: {sum(bakery.values())}")
