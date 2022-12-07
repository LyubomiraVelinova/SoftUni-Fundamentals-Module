cards = input().split(" ")
shuffle_count = int(input())
middle_length = len(cards) // 2

for i in range(shuffle_count):
    result = []

    for index in range(middle_length):
        first_card = cards[index]

        current_index_second_deck = index + middle_length
        second_card = cards[current_index_second_deck]

        result.append(first_card)
        result.append(second_card)

    cards = result
print(cards)

# for every_shuffle in range(shuffle_count):
#     index = 0
#     shuffled_strings = []
#
#     for every_string in range(len(cards)):
#         shuffled_strings.append(cards[index])
#         shuffled_strings.append(cards[index + int(len(cards) / 2)])
#         index += 1
#
#         if index == int(len(cards) / 2):
#             cards = shuffled_strings
#             break
#
# print(shuffled_strings)
