ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLANDS = 3
TREE_LIGHTS = 15

quantity = int(input())
days = int(input())

counter = 0
total_spirit = 0
budget = 0

while days > 0:
    counter += 1
    days -= 1
    if counter % 11 == 0:
        quantity += 2
    # Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
    if counter % 2 == 0:
        total_spirit += 5
        budget += ORNAMENT_SET * quantity
    # Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
    if counter % 3 == 0:
        total_spirit += 13
        budget += (TREE_SKIRT + TREE_GARLANDS) * quantity
    # Every fifth day you buy Tree Lights quantity of times and increase your Christmas spirit by 17. If you have bought
    # Tree Skirts and Tree Garlands at the same day you additionally increase your spirit by 30.
    if counter % 5 == 0:
        total_spirit += 17
        budget += (TREE_LIGHTS) * quantity
    if counter % 3 == 0 and counter % 5 == 0:
        total_spirit += 30
    if counter % 10 == 0:
        total_spirit -= 20
        budget += TREE_SKIRT + TREE_GARLANDS + TREE_LIGHTS
        # Also if the last day is a tenth day the cat decides to demolish even more and ruins the Christmas turkey and you lose additional 30 spirit.
        if days == 0:
            total_spirit -= 30

print(f"Total cost: {budget}\nTotal spirit: {total_spirit}")
