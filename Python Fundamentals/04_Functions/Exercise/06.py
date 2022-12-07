password = input()


def valid(a):
    digits_counter = 0
    letters_counter = 0

    if 6 <= len(a) <= 10:
        for char in a:
            if char.isdigit():
                digits_counter += 1
            elif char.isalpha():
                letters_counter += 1
            else:
                print("Password must consist only of letters and digits")
            if digits_counter >= 2 and letters_counter > 0:
                print("Password is valid")

    else:
        print("Password must be between 6 and 10 characters")
    if digits_counter < 2:
        print("Password must have at least 2 digits")


print(valid(password))
