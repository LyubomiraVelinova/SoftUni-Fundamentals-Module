# def char_position(letter: str):
#     result = 0
#     if letter.isupper():
#         result = ord(letter) - 64
#     elif letter.islower():
#         result = ord(letter) - 96
#     return result

def char_position(letter: str):
    lower_letter = letter.lower()
    return ord(lower_letter) - 96


def first_letter_operation(letter: str, num: int):
    result = 0
    if letter.isupper():
        result = num / char_position(letter)
    elif letter.islower():
        result = num * char_position(letter)
    return result


def last_letter_operation(letter: str, num: int):
    if letter.isupper():
        num -= char_position(letter)
    elif letter.islower():
        num += char_position(letter)
    return num


line_input = input().split()
total = 0
for string in line_input:
    resulted_num = 0
    first_letter = string[0]
    last_letter = string[-1]
    num = int(string[1:-1])
    resulted_num += first_letter_operation(first_letter, num)
    total += last_letter_operation(last_letter, resulted_num)

print(f"{total:.2f}")
