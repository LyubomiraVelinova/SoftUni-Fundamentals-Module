words = input().split()
first_word = words[0]
second_word = words[1]
total_sum = 0

min_length = min(len(first_word), len(second_word))

for i in range(min_length):
    result = ord(first_word[i]) * ord(second_word[i])
    total_sum += result

biggest_word = first_word
if len(second_word) > len(first_word):
    biggest_word = second_word

for i in range(min_length, len(biggest_word)):
    total_sum += ord(biggest_word[i])

print(total_sum)
