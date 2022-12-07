number_sheeps = int(input())
message = ""

for sheep in range(1, number_sheeps + 1):
    message += f"{sheep} sheep..."

print(message)