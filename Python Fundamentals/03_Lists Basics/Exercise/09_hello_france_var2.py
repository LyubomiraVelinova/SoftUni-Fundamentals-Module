data = input().split("|")
budget = float(input())

profit = 0
new_budget = 0

for d in data:
    item = d.split("->")[0]
    price = float(d.split("->")[1])
    is_in_range = False

    if item == "Clothes" and price <= 50:
        is_in_range = True
    elif item == "Shoes" and price <= 35:
        is_in_range = True
    elif item == "Accessories" and price <= 20.50:
        is_in_range = True

    if is_in_range:
        if budget - price < 0:
            continue
        else:
            budget -= price
            profit += 0.40 * price
            price += 0.40 * price
            new_budget += price
            print(f"{price:.2f}", end=" ")

print(f"Profit: {profit:.2f}")

if budget + new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")