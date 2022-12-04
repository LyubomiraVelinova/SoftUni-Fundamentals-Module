import re

pattern = r"((^|(?<=\s))(-*)(\d+)((\.\d+)*)($|(?=\s)))"

text = input()
matches = re.findall(pattern, text)

for match in matches:
    number, *others = match
    print(number, end=" ")
