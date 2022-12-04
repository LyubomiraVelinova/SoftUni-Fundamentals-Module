wolf_or_sheep = input()
list_of_wolf_or_sheep = wolf_or_sheep.split(", ")

if list_of_wolf_or_sheep [-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(list_of_wolf_or_sheep)-1}! You are about to be eaten by a wolf!")