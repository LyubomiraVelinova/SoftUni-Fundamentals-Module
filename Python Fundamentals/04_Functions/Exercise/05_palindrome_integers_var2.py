def get_palindrome(a):
    for every_num in list_of_integers:
        if every_num == every_num[::-1]:
            return True
        else:
            return False


list_of_integers = input().split(", ")
print(get_palindrome(list_of_integers))