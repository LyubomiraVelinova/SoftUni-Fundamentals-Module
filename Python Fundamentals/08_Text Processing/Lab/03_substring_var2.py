def replace_all(replace_str, actual_str):
    while replace_str in actual_str:
        actual_str = actual_str.replace(replace_str, "")
    return actual_str

print(replace_all(input(), input()))
