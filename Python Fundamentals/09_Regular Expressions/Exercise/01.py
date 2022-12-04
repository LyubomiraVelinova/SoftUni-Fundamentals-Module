import re

pattern = "\d+"

while True:
    test_str = input()

    if not test_str:
        break

    matches = re.findall(pattern, test_str)
    for match in matches:
        print(match, end=" ")
