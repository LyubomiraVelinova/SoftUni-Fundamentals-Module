fire_levels = input().split("#")
water_amount = int(input())

total_efford = 0
every_level = []
total_fire = 0

print("Cells:")

for i in fire_levels:
    if water_amount > 0:
        every_level = i.split(" = ")
        cell = int(every_level[1])
        efford = 0.25
        if "Low" in every_level:
            if 1 <= cell <= 50:
                if cell <= water_amount:
                    water_amount -= cell
                    efford *= cell
                    total_fire += cell
                    total_efford += efford
                    print(f" - {cell}")
                else:
                    continue

        elif "Medium" in every_level:
            if 51 <= cell <= 80:
                if cell <= water_amount:
                    water_amount -= cell
                    efford *= cell
                    total_fire += cell
                    total_efford += efford
                    print(f" - {cell}")
                else:
                    continue

        elif "High" in every_level:
            if 81 <= cell <= 125:
                if cell <= water_amount:
                    water_amount -= cell
                    efford *= cell
                    total_fire += cell
                    total_efford += efford
                    print(f" - {cell}")
                else:
                    continue

print(f"Effort: {total_efford:.2f}\nTotal Fire: {total_fire}")