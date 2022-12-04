data = input().split()

products = {data[index]: int(data[index+1]) for index in range(0, len(data), 2)}

# for index in range(0, len(data), 2):
#     product_name = data[index]
#     product_quantity = int(data[index+1])
#     products[product_name] = product_quantity

print(products)