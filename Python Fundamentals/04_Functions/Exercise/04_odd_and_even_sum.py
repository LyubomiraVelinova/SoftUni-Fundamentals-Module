number = int(input())


def odd_and_even_sum(number):
    number_to_str = str(number)
    sum_even = 0
    sum_odd = 0
    for i in range(len(number_to_str)):
        odd_or_even_num = int(number_to_str[i])
        if odd_or_even_num % 2 == 0:
            sum_even += odd_or_even_num
        elif odd_or_even_num % 2 != 0:
            sum_odd += odd_or_even_num
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"

print(odd_and_even_sum(number))