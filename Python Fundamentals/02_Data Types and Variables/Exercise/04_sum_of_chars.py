n = int(input())

total_sum = 0
for every_line in range (n):
    letter = input()
    letter_to_ASCII = ord(letter)
    total_sum += letter_to_ASCII

print(f"The sum equals: {total_sum}")