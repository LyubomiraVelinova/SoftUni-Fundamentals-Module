line = input()
sides = {}

while line != "Lumpawaroo":
    if " | " in line:
        args = line.split(" | ")
        side = args[0]
        user = args[1]

        if side not in sides:
            sides[side] = []

        all_values = []
        for current in sides.values():
            all_values += current

        if user not in all_values:
            sides[side].append(user)

    else:
        args = line.split(" -> ")
        side = args[1]
        user = args[0]
        old_side = ""

        for key, value in sides.items():
            if user in value:
                old_side = key
                break

        if old_side != "":
            sides[old_side].remove(user)

            if side not in sides:
                sides[side] = []
            sides[side].append(user)

        else:
            if side not in sides:
                sides[side] = []

            sides[side].append(user)

        print(f"{user} joins the {side} side!")

    line = input()

sorted_force_book = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))


for key, people in sorted_force_book.items():
    if len(people) == 0:
        continue
    print(f"Side: {key}, Members: {len(people)}")
    for person in sorted(people):
        print(f"! {person}")
