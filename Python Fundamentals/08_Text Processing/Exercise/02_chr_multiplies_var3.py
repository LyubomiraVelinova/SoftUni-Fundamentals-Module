line_input = input().split()
str_1 = line_input[0]
str_2 = line_input[1]


def character_codes_multiplied(first: str, second: str, length: int):
    sum = 0
    for i in range(length):
        sum += ord(first[i]) * ord(second[i])
    return sum


def remaining_characters(chars: str):
    sum = 0
    for ch in chars:
        sum += ord(ch)
    return sum


length = 0
chars = ''
if len(str_1) == len(str_2):
    length = len(str_2)
    result = character_codes_multiplied(str_1, str_2, length)
else:
    if len(str_1) > len(str_2):
        length = len(str_2)
        chars = str_1[length:]
    elif len(str_1) < len(str_2):
        length = len(str_1)
        chars = str_2[length:]
    result = character_codes_multiplied(str_1, str_2, length) + remaining_characters(chars)

print(result)
