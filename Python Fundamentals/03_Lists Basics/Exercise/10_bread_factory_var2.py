events = input().split("|")

energy = 100
coins = 100
is_bankrupt = False

for every_event in events:
    args = every_event.split("-")
    name_or_item = args[0]
    value = int(args[1])

    if name_or_item == "rest":
        gained_energy = 0
        if energy + value < 100:
            gained_energy = value
            energy += value
        else:
            gained_energy = 100 - energy
            energy = 100
        print(f"You gained {gained_energy} energy.\nCurrent energy: {energy}.")

    elif name_or_item == "order":
        if energy < 30:
            energy += 50
            print(f"You had to rest!")
            continue

        coins += value
        energy -= 30
        print(f"You earned {value} coins.")
    else:
        if coins <= value:
            print(f"Closed! Cannot afford {name_or_item}.")
            is_bankrupt = True
            break
        coins -= value
        print(f"You bought {name_or_item}.")

if not is_bankrupt:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
