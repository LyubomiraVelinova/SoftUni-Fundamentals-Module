n = int(input())

for num in range(1, n + 1):
    is_special = False
    if num < 10:
        sum_of_digits = num
    else:
        sum_of_digits = int(num / 10) + num % 10

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True

    print(f"{num} -> {is_special}")


