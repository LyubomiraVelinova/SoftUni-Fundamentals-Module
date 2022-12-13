words = input().split()
palindrome = input()


def find_palindrome(word):
    is_palindrome = True
    for index in range(len(word)):
        if word[index] != word[- index - 1]:
            is_palindrome = False
            break
    if is_palindrome:
        return word


def find_occurrences(words: list, word):
    occurrences = 0
    for w in words:
        if w == word:
            occurrences += 1

    return occurrences

list_of_palindromes = [find_palindrome(word) for word in words if find_palindrome(word) != None]

count_occurrences = find_occurrences(words, palindrome)
print(f"{list_of_palindromes}\nFound palindrome {count_occurrences} times")
