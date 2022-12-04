def all_digits(text):
    digits = ""
    for char in text:
        if char.isdigit():
            digits += char
    return digits


def all_letters(text):
    letters = ""
    for char in text:
        if char.isalpha():
            letters += char
    return letters


def all_other_characters(text):
    other_characters = ""
    for char in text:
        if not char.isalpha() and not char.isdigit():
            other_characters += char
    return other_characters


text = input()

print(all_digits(text))
print(all_letters(text))
print(all_other_characters(text))
