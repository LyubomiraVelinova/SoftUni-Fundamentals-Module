a = input()
b = input()


def characters(a, b):
    for all_char in range(ord(a) + 1, ord(b)):
        print(chr(all_char), end=" ")


characters(a, b)