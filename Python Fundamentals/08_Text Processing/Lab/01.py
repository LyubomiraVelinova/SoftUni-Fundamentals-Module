def reverse(string):
    return string[::-1]

words = []
while True:
    command = input()
    if command == "end":
        break
    words.append(command)

for word in words:
    print(f"{word} = {reverse(word)}")