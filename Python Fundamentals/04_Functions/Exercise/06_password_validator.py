def length(word):
    if 6 <= len(word) <= 10:
        return is_validate
    else:


def only_letters_and_digits(word):
    for every_char in word:
        if 48 <= chr(every_char) <= 57 or 65 <= chr(every_char) <= 90 or 97 <= chr(every_char) <= 122:
            return is_validate


def two_digits(word):
    counter = 0
    for every_char in word:
        if 48 <= chr(every_char) <= 57:
            counter += 1
        if counter >= 2:
            return is_validate


def solve(word):

password = input()
is_validate = True
print valid_password(password)