import re


pattern = r">>([A-Za-z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"
total_price = 0
print(f"Bought furniture:")

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.fullmatch(pattern, line)

    if match is None:
        continue

    print(match[1])
    price = float(match[2])
    quantity = int(match[4])

    total_price += price * quantity

print(f"Total money spend: {total_price:.2f}")
