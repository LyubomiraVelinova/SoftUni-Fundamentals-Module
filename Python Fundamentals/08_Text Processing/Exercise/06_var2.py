line = input()

for i in range(len(line)):
    ch = line[i]
    if i + 1 == len(line):
        print(ch, end="")
        break

    next_ch = line[i + 1]

    if ch != next_ch:
        print(ch, end="")
