import re

text = input()
key_word = input()

pattern = rf"\b{key_word}\b"

matches = re.findall(pattern, text, re.IGNORECASE)
print(len(matches))
