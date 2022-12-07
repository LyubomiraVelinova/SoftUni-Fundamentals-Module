a = int(input())
b = int(input())
c = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def solve(a, b, c):
    sum = sum_numbers(a, b)
    res = subtract(sum, c)
    return res


res = solve(a, b, c)
print(res)
