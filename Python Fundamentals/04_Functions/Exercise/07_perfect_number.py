number = int(input())


def perfect_number(a):
    divisors = 1
    for i in range(2, a):
        if number % i == 0:
            divisors += i

    if divisors == a:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect_number(number))