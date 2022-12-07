first_word = input()
second_word = input()

list_words = []

for i in range(len(second_word)):
    letter = second_word[i]
    first_word = first_word.replace(first_word[i], second_word[i], 1)
    if first_word not in list_words:
        list_words.append(first_word)
for word in list_words:
    print(word)
