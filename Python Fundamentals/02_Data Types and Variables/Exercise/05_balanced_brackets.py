n = int(input())

balance = 0
brackets = 0
for i in range(n):
    string = input()
    if string == "(":
        balance += 1
        brackets += 1
    elif string == ")" and 0 <= brackets < 2:
        balance -= 1
        brackets -= 1

if balance == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
