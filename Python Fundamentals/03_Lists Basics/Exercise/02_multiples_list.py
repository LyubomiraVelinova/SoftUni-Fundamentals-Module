factor = int(input())
count = int(input())

end_of_the_range = factor * count
multiples_of_the_factor = []

for number in range(factor, end_of_the_range + 1):
    if number % factor == 0:
        multiples_of_the_factor.append(number)

print(multiples_of_the_factor)
