import re

total_price = 0
furnitures = []
while True:
    line = input()
    if line == "Purchase":
        break

    pattern = r">>([A-Za-z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"
    match = re.fullmatch(pattern, line)

    if match is None:
        continue

    furniture = match[1]
    price = float(match[2])
    quantity = int(match[4])

    total_price += price * quantity
    furnitures.append(furniture)

print(f"Bought furniture:")
print(f"\n".join(furnitures))
print(f"Total money spend: {total_price:.2f}")
