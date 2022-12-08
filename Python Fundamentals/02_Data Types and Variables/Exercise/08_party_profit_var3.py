from math import floor

party_size = int(input())
days = int(input())

coins = 0
counter = 0
companions_count = party_size

while days > 0:
    counter += 1
    coins += 50

    if counter % 10 == 0:
        companions_count -= 2
    if counter % 15 == 0:
        companions_count += 5
    if counter % 3 == 0:
        coins -= 3 * companions_count
    if counter % 5 == 0:
        coins += 20 * companions_count
    if counter % 3 == 0 and counter % 5 == 0:
        coins -= 2 * companions_count

    coins -= 2 * companions_count
    days -= 1

print(f"{companions_count} companions received {floor(coins / companions_count)} coins each.")
