from collections import  defaultdict
products_quantity = defaultdict(int)
products_price = defaultdict(int)

while True:
    line_input = input()
    if line_input == "buy":
        break

    product, price, quantity = line_input.split()
    products_quantity[product] += int(quantity)
    products_price[product] = float(price)

for product_name, quantity in products_quantity.items():
    print(f"{product_name} -> {(quantity * products_price[product_name]):.2f}")
