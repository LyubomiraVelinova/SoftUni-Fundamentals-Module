num = int(input())


def loading_bar(num):
    counter = num // 10
    loading_bar = ""
    if counter < 10:
        for sign in range(counter):
            loading_bar += "%"
        for d in range(10 - counter):
            loading_bar += "."

        return f"{num}% [{loading_bar}]\nStill loading..."
    elif counter == 10:
        return f"100% Complete!\n[%%%%%%%%%%]"

print(loading_bar(num))
