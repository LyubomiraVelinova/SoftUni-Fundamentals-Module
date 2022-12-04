party_size = int(input())
days = int(input())

earn = 0
spent = 0
for every_day in range(1, days + 1):

    if every_day % 10 == 0:
        party_size -= 2
    if every_day % 15 == 0:
        party_size += 5
        spent += 2 * party_size
    if every_day % 3 == 0:
        spent += 3 * party_size
    if every_day % 5 == 0:
        earn += 20 * party_size

    earn += 50
    spent += 2 * party_size

coin_per_party = (earn - spent) // party_size
print(f"{party_size} companions received {coin_per_party} coins each.")