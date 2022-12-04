n = int(input())

for first in range(n):
    for second in range(n):
        for third in range(n):
            print(f"{chr(first+97)}{chr(second+97)}{chr(third+97)}")
