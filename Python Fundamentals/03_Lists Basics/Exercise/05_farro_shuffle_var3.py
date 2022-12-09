word = input()
times = int(input())

cards_deck = word.split(" ")

for time in range(times):
    shuffled_cards_deck = []
    for i in range(0, int(len(cards_deck) / 2)):
        shuffled_cards_deck.append(cards_deck[i])
        shuffled_cards_deck.append(cards_deck[i + int(len(cards_deck) / 2)])
    cards_deck = shuffled_cards_deck

print(shuffled_cards_deck)
