text = input()
while text != "end":
    word = text
    word_reversed = ""
    for ch in reversed(word):
        word_reversed += ch

    print(word + " = " + word_reversed)
    text= input()