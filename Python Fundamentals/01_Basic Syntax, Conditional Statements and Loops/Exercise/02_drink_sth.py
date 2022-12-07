years = int(input())
kind_of_drink= ""

if years <= 14:
    kind_of_drink = "toddy"
elif years <= 18:
    kind_of_drink = "coke"
elif years <= 21:
    kind_of_drink = "beer"
else:
    kind_of_drink = "whisky"

print(f"drink {kind_of_drink}")