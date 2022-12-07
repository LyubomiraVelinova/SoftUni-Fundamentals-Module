first_num = int(input())
second_num = int(input())
third_num = int(input())


def get_smallest_of_three(first_num, second_num, third_num):
    smallest = first_num
    if second_num < smallest:
        smallest = second_num
    if third_num < smallest:
        smallest = third_num
    return smallest


print(get_smallest_of_three(first_num, second_num, third_num))