def get_smallest_of_three_numbers(a, b, c):
    smallest = min(a, b, c)
    return smallest


a = int(input())
b = int(input())
c = int(input())

print(get_smallest_of_three_numbers(a, b, c))