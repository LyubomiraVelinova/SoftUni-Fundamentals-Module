budget = float(input())
price_flour = float(input())

price_eggs = 0.75 * price_flour
price_milk_for_cozonac = (1.25 * price_flour) / 4

price_for_one_cozonac = price_flour + price_eggs + price_milk_for_cozonac

coloured_eggs = 0
current_cozonacs = 0

count_cozonac = int(budget // price_for_one_cozonac)
for every_cozonac in range(1,count_cozonac+1):
    coloured_eggs += 3
    current_cozonacs += 1
    if current_cozonacs % 3 == 0:
        coloured_eggs = coloured_eggs - (current_cozonacs - 2)

print(f"You made {count_cozonac} cozonacs! Now you have {coloured_eggs} eggs and {budget-price_for_one_cozonac*count_cozonac:.2f}BGN left.")
