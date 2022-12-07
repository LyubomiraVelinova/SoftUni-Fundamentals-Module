a = int(input())
b = int(input())


def factorial_of_two(a, b):
    factorial_of_first = 1
    factorial_of_second = 1
    for i in range(a, 0, -1):
        factorial_of_first *= i
    for j in range(b, 0, -1):
        factorial_of_second *= j

    result = factorial_of_first / factorial_of_second
    return result


print(f"{factorial_of_two(a, b):.2f}")
