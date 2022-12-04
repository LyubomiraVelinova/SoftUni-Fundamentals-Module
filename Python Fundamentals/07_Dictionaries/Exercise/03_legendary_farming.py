key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
sth_obtained = False

while sth_obtained is False:
    line = input().split()

    for items in range(0, len(line), 2):
        material = line[items + 1].lower()
        quantity = int(line[items])

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                if material == "shards":
                    print("Shadowmourne obtained!")
                elif material == "fragments":
                    print("Valanyr obtained!")
                elif material == "motes":
                    print("Dragonwrath obtained!")

                key_materials[material] -= 250
                sth_obtained = True
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

sorted_key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
sorted_junk = dict(sorted(junk.items(), key=lambda a: a[0]))

for key, value in sorted_key_materials.items():
    print(f"{key}: {value}")
for key, value in sorted_junk.items():
    print(f"{key}: {value}")
