lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
shield_brakes_count = 0

for lost_game in range(1, lost_fights_count + 1):
    # Every second lost game, his helmet is broken.
    if lost_game % 2 == 0:
        total_expenses += helmet_price

    #Every third lost game, his sword is broken.
    if lost_game % 3 == 0:
        total_expenses += sword_price

    #When both his sword and helmet are broken in the same lost fight, his shield also brakes.
    if lost_game % 2 == 0 and lost_game % 3 == 0:
        total_expenses += shield_price
        shield_brakes_count += 1
        if shield_brakes_count % 2 == 0:
            total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")

