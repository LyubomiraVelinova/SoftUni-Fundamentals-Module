def next_char_is_digit(sequence):
    is_digit = False
    for i in range(len(sequence)):
        if i < len(sequence) - 1:
            if (sequence[i]).isdigit():
                if (sequence[i+1]).isdigit():
                    is_digit = True
                break
    return is_digit


str_num_sequence = input()
unique_symbols = []
rage_message = ""
while len(str_num_sequence) > 0:
    str_sequence = ""
    num_sequence = ""
    for index in range(len(str_num_sequence)):
        char = str_num_sequence[index]
        if char.isdigit():
            num_sequence += char
            if next_char_is_digit(str_num_sequence):
                num_sequence += str_num_sequence[index + 1]
                str_num_sequence = str_num_sequence[index + 2:]
                break
            else:
                str_num_sequence = str_num_sequence[index + 1:]
                break
        else:
            str_sequence += char
            if char.upper() not in unique_symbols:
                unique_symbols.append(char.upper())
    rage_message += (str_sequence.upper() * int(num_sequence))

print(f"Unique symbols used: {len(unique_symbols)}\n{rage_message}")
