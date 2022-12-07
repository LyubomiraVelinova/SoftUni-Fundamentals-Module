budget = float(input())
price_kg_flour = float(input())

# The price for 1 pack of eggs is 75% of the price for 1 kg flour.
price_pack_of_eggs = 0.75 * price_kg_flour
# The price for 1l milk is 25% more than price for 1 kg flour.
price_l_milk = 1.25 * price_kg_flour
# Notice, that you need 0.250l milk for one cozonac and the calculated price is for 1l.
cozonac_price = price_pack_of_eggs + price_kg_flour + 0.25 * price_l_milk

counter = 0
colored_eggs = 0

while budget - cozonac_price > 0:
    counter += 1
    budget -= cozonac_price
    colored_eggs += 3
    if counter % 3 == 0:
        colored_eggs -= (counter - 2)

print(f"You made {counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
