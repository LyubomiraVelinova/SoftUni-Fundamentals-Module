#НЕ Е КОРЕКТЕН!
number = int(input())

for num in range(number, 10000):
    str_to_num = str(num)
    if str_to_num[0] != str_to_num[1] and str_to_num[0] != str_to_num[2] and str_to_num[0] != str_to_num[3]:
        if str_to_num[1] != str_to_num[2] and str_to_num[1] != str_to_num[3]:
            if str_to_num[2] != str_to_num[3]:
                print(f"{num}")
                break

#for first_num in range(10):
    #for second_num in range(10):
        #for third_num in range(10):
            #for forth_num in range(10):
#while true


