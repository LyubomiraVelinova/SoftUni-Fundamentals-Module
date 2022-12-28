text = input().split()
new_word = ""
for word in text:
    new_word += word * len(word)

print(new_word)
