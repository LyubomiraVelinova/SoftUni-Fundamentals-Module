replace_str = input()
actual_str = input()

while replace_str in actual_str:
    actual_str = actual_str.replace(replace_str, "")

print(actual_str)