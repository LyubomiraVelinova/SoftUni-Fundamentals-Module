list_of_line = []
products = {}

while True:
    line = input()
    if line == "stop":
        break

    list_of_line.append(line)

for every_odd in range(0, len(list_of_line), 2):
    products[list_of_line[every_odd]] = list_of_line[every_odd + 1]

for key,value in products.items():
    print(f"{key} -> {value}")