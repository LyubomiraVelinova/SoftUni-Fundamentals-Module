from collections import defaultdict

line_input = input().split()
word_appearance = defaultdict(int)

for word in line_input:
    word_lowercase = word.lower()
    word_appearance[word_lowercase] += 1

filtered_list = [key for key, value in word_appearance.items() if value % 2 != 0]
print(f"{' '.join(filtered_list)}")
# filtered_words = filter(lambda value: value % 2 == 1, word_appearance.values())
# print(filtered_words)