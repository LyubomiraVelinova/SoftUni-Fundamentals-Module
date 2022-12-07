budget = float(input())
price_flour = float(input())

price_eggs = 0.75 * price_flour
price_milk_for_cozonac = (1.25 * price_flour) / 4

price_for_one_cozonac = price_flour + price_eggs + price_milk_for_cozonac

coloured_eggs = 0
current_cozonacs = 0

while budget >= price_for_one_cozonac:
    coloured_eggs += 3
    current_cozonacs += 1
    if current_cozonacs % 3 == 0:
        coloured_eggs -= (current_cozonacs - 2)

    budget -= price_for_one_cozonac

print(f"You made {current_cozonacs} cozonacs! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
