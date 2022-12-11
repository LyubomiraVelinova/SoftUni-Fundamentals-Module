first_num = int(input())
second_num = int(input())


def calculate_factorial(num):
    factorial = 1
    for n in range(num, 0, -1):
        factorial *= n
    return factorial


def dividing_nums(first_num, second_num):
    division = f"{(first_num / second_num):.2f}"
    return division


print(dividing_nums(calculate_factorial(first_num), calculate_factorial(second_num)))