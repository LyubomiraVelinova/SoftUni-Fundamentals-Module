lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0

for every_lost_fight in range(1, lost_fights_count + 1):
    if every_lost_fight % 2 == 0:
        broken_helmet += 1
    if every_lost_fight % 3 == 0:
        broken_sword += 1
    if every_lost_fight % 6 == 0:
        broken_shield += 1
        if broken_shield % 2 == 0:
            broken_armor += 1

expenses = broken_helmet * helmet_price + broken_sword * sword_price + broken_shield * shield_price + broken_armor * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")