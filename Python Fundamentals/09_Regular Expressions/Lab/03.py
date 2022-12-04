import re

pattern = r"(\d{2})([\/\.-])([A-Z][a-z]{2})\2(\d{4})"
text = input()
matches = re.findall(pattern,text)

for match in matches:
    day, _, month, year = match
    print(f"Day: {day}, Month: {month}, Year: {year}")