import operator


def sum_numbers(first_int: int, second_int: int):
    sum_of_two = operator.add(first_int, second_int)
    return sum_of_two


def subtract(sum_of_nums, third_int: int):
    result = sum_of_nums - third_int
    return result


first = int(input())
second = int(input())
third = int(input())
sum_of_two = sum_numbers(first, second)
print(subtract(sum_of_two, third))
