cards = input().split(" ")
shuffle_count = int(input())

for every_shuffle in range(shuffle_count):
    index = 0
    # index_2 = index + int(len(single_string)/2)
    shuffled_strings = []

    for every_string in range(len(cards)):
        shuffled_strings.append(cards[index])
        shuffled_strings.append(cards[index + int(len(cards) / 2)])
        index += 1

        # max index = len(single_string) - 1
        if index == int(len(cards) / 2):
            cards = shuffled_strings
            break

print(shuffled_strings)