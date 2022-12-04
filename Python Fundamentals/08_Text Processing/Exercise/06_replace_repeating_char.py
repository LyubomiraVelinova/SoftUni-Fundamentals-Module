text = input()
current_char = 0
new_input = ""
for char in text:
    if ord(char) != current_char:
        new_input += char
        current_char = ord(char)

print(new_input)
