key = int(input())
lines = int(input())

for i in range(lines):
    characters = input()
    number = (ord(characters) + key)
    print(chr(number), end="")