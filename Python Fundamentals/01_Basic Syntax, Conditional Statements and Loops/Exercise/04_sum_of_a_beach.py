word = input()
new_word = word.lower()

coincidence = 0

while len(new_word) >= 3:
    if "water" in new_word:
        coincidence += 1
        new_word = new_word.lstrip("water")
    if "fish" in new_word:
        coincidence += 1
        new_word = new_word.lstrip("fish")
    if "sun" in new_word:
        coincidence += 1
        new_word = new_word.lstrip("sun")
    if "sand" in new_word:
        coincidence += 1
        new_word = new_word.lstrip("sand")

print(coincidence)