number = int(input())


def loading_bar(a):
    percent_counter = 0
    loading_list = []
    for i in range(a // 10):
        percent_counter += 1
        percent_sign = "%"
        loading_list.append(percent_sign)
    residue = 10 - percent_counter
    for j in range(residue):
        point_sign = "."
        loading_list.append(point_sign)

    if percent_counter == 10:
        new_loading_list = "".join(loading_list)
        return f"100% Complete!\n[{new_loading_list}]"
    else:
        new_loading_list = "".join(loading_list)
        return f"{a}% [{new_loading_list}]\nStill loading..."


print(loading_bar(number))
