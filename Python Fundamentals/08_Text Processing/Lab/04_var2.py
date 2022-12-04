from functools import reduce

banned_words = input().split(", ")
text = input()
# text = reduce(lambda a,b: text.replace(a, "*"*len(a)))
# ??? Try to do it!
print(text)
