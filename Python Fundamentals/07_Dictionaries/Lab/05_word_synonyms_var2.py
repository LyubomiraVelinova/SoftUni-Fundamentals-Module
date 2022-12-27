from collections import defaultdict

synonyms = defaultdict(list)
n = int(input())
for count in range(n):
    word = input()
    synonym = input()
    synonyms[word].append(synonym)

for word, synonym in synonyms.items():
    print(f"{word} - {', '.join(synonym)}")
