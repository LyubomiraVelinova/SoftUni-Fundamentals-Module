line_input = input().split()


def switched_letters(word: str):
    # list_of_word = [letter for letter in word]
    # second_letter = ""
    # counter = -1
    # for l in word:
    #     counter += 1
    #     if l.isalpha():
    #         second_letter = l
    #         break
    # last_letter = list_of_word[-1]
    # list_of_word[counter] = last_letter
    # list_of_word[-1] = second_letter

    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return "".join(temp)


def first_letter_char(word: str):
    num = ""
    for l in word:
        if l.isnumeric():
            num += l
    letter = chr(int(num))
    new_word = f"{letter}"
    for l in word:
        if l.isalpha():
            new_word += l
    return new_word


decipher = []
for word in line_input:
    word_decipher = first_letter_char(word)
    new_word = switched_letters(word_decipher)
    decipher.append(new_word)

print(" ".join(decipher))
