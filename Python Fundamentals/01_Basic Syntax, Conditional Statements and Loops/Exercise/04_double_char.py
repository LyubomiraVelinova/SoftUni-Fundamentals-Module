word = input()
repeated_letter = ""
repeated_word = ""

for i in range (len(word)):
    repeated_letter = word [i] * 2
    repeated_word += repeated_letter

print(f"{repeated_word}",end = "")