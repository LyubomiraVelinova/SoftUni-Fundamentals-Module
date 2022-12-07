items = input().split("|")
budget = float(input())

CLOTHES = 50
SHOES = 35
ACCESSORIES = 20.50
TICKETS = 150

bought = 0
new_budget = 0
new_prices = []
every_item = []

for i in items:
    every_item = i.split("->")
    price = float(every_item[1])
    item = every_item[0]

    if ("Clothes" == item and price <= CLOTHES) or ("Shoes" == item and price <= SHOES) or ("Accessories" == item and price <= ACCESSORIES):
        if price <= budget:
            budget -= price
            bought += price
            new_budget += 1.40 * price
            new_prices.append(f"{1.40 * price:.2f}")

print(*new_prices)
print(f"Profit: {(new_budget - bought):.2f}")

if budget + new_budget >= TICKETS:
    print("Hello, France!")
else:
    print("Time to go.")