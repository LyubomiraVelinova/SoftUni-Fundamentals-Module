import re

pattern = r"\b_([a-zA-Z0-9]+)\b"

text = input()

matches = re.finditer(pattern, text)
all_names = [m[1] for m in matches]
print(",".join(all_names))
