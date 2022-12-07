divisor = int(input())
bound = int(input())

largest_num = 0

for N in range(divisor, bound+1):
    if N % divisor == 0 and N > 0 and N <= bound:
        if N >= largest_num:
            largest_num = N

print(f"{largest_num}")