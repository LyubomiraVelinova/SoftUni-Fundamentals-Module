text = input().split()
first_str = text[0]
second_str = text[1]
result = 0
if len(first_str) == len(second_str):
    for i in range(len(first_str)):
        result += ord(first_str[i]) * ord(second_str[i])
elif len(first_str) > len(second_str):
    # remaining_chr = len(first_str) - len(second_str)
    for j in range(len(second_str)):
        result += ord(first_str[j])*ord(second_str[j])

    for i in range(len(second_str), len(first_str)):
        result += ord(first_str[i])
elif len(second_str) > len(first_str):
    for j in range(len(first_str)):
        result += ord(first_str[j])*ord(second_str[j])
    for i in range(len(first_str), len(second_str)):
        result += ord(second_str[i])

print(result)
