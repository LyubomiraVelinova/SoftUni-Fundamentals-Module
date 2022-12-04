def calculate(product_name: str, product_quantity: int):
    price = None
    if product_name == "coffee":
        price = 1.5
    elif product_name == "water":
        price = 1
    elif product_name == "coke":
        price = 1.4
    elif product_name == "snacks":
        price = 2

    if price is not None:
        return price * product_quantity


product_name = input()
product_quantity = int(input())
print(f"{calculate(product_name, product_quantity):.2f}")
