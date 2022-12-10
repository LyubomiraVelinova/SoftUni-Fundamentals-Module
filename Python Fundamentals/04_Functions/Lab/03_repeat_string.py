def repeat_string(old_string: str, n: int):
    new_string = ""
    for time in range(n):
        new_string += old_string

    return new_string


old_string = input()
n = int(input())

print(repeat_string(old_string, n))
