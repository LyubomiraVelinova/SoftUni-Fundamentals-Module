text = input().split("\\")
string = (text[-1]).split(".")
extension = string[1]
name = string[0]
print(f"File name: {name}\nFile extension: {extension}")