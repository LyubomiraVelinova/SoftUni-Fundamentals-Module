quantity = int(input())
days = int(input())

ornament_set_piece = 2
tree_skirt_piece = 5
tree_garlands_piece = 3
tree_lights_piece = 15

budget = 0
Christmas_spirit = 0

for every_day in range(1, days + 1):
    if every_day % 11 == 0:
        quantity += 2

    if every_day % 2 == 0:
        budget += ornament_set_piece * quantity
        Christmas_spirit += 5

    if every_day % 3 == 0:
        budget += tree_skirt_piece * quantity + tree_garlands_piece * quantity
        Christmas_spirit += 13

    if every_day % 5 == 0:
        budget += tree_lights_piece * quantity
        Christmas_spirit += 17

    if every_day % 15 == 0:
        Christmas_spirit += 30

    if every_day % 10 == 0:
        Christmas_spirit -= 20
        budget += (tree_skirt_piece + tree_garlands_piece + tree_lights_piece)

if days % 10 == 0:
    Christmas_spirit -= 30

print(f"Total cost: {budget}\nTotal spirit: {Christmas_spirit}")
