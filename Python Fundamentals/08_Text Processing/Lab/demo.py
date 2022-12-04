# n = "lorem"
# print(n[-1:-3:-1])
#
# s = """jhaujgah
# ahaoia
# nkahaia"""
#
# print(s)

first_string = input()
second_string = input()


while first_string in second_string:
    second_string = second_string.replace(first_string, "")

print(second_string)