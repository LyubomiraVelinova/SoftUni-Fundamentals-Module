events = input().split("|")
energy = 100
coins = 100

are_the_events_handled = True

for every_event in events:
    split_events = every_event.split("-")
    name_or_item = split_events[0]
    number = int(split_events[1])
    gained_energy = 0
    earned_coins = 0
    if name_or_item == "rest":
        if energy < 100:
            gained_energy += number
            energy += gained_energy
            if energy > 100:
                gained_energy = gained_energy - (energy-100)
                energy = 100
        print(f"You gained {gained_energy} energy.\nCurrent energy: {energy}.")
    elif name_or_item == "order":
        if energy >= 30:
            earned_coins += number
            coins += earned_coins
            energy -= 30
            print(f"You earned {earned_coins} coins.")
        else:
            energy += 50
            are_the_events_handled = False
            print(f"You had to rest!")
    else:
        if coins > number:
            coins -= number
            print(f"You bought {name_or_item}.")
        else:
            are_the_events_handled = False
            print(f"Closed! Cannot afford {name_or_item}.")
            break

if are_the_events_handled:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
