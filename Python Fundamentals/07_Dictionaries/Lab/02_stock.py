#Step 1: Build products
data = input().split()

products = {data[index]: int(data[index+1]) for index in range(0, len(data), 2)}

search_products = input().split()
for search_product in search_products:
    if search_product in products:
        #We have the product available
        quantity = products[search_product]
        print(f"We have {quantity} of {search_product} left")
    else:
        #The product is not available
        print(f"Sorry, we don't have {search_product}")