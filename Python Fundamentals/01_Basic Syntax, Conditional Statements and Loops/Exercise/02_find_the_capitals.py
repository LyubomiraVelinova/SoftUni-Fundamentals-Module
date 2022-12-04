s = input()

capital_indexes = []

for i in range (len(s)):
    char = s[i]
    if char.isupper():
        capital_indexes.append(i)

print(capital_indexes)