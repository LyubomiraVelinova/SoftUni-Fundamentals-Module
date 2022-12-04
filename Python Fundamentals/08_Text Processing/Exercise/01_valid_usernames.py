#
# def valid_lenght(name):
#     if 3 < len(name) < 16:
#         for i in name:
#             if i.isalpha() or i.isdigit() or i.ishyphens() or i.isundercores():
#                 return valid_names.append(name)


names = input().split(", ")
valid_names = []

for name in names:
    if 3 < len(name) < 16:
        counter = 0
        for i in name:
            if i.isalnum() or i == "-" or i == "_":
                counter += 1
                if counter == len(name):
                    valid_names.append(name)
            else:
                break

print("\n".join(valid_names))
