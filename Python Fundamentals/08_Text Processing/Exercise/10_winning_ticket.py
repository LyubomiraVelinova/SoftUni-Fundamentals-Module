def is_valid(char: str):
    is_valid = False
    if len(char) == 20:
        is_valid = True
    return is_valid


def number_of_symbol_repetition(ticket: str, winning_symbols: list):
    left_count = 0
    right_count = 0
    match_symbol = ""
    for symbol in winning_symbols:
        left_side_of_ticket = ticket[:int(len(ticket) / 2)]
        right_side_of_ticket = ticket[int(len(ticket) / 2):]
        if symbol in (left_side_of_ticket and right_side_of_ticket):
            match_symbol = symbol
            left_count = left_side_of_ticket.count(symbol)
            right_count = right_side_of_ticket.count(symbol)
            break

    return left_count, right_count, match_symbol


line_input = input().split(", ")
WINNING_SYMBOLS = ['@', '#', '$', '^']

for char in line_input:
    if is_valid(char):
        match_length_left, match_length_right, match_symbol = number_of_symbol_repetition(char, WINNING_SYMBOLS)
        if match_length_left == match_length_right:
            match_length = match_length_left
            if 10 > match_length >= 6:
                print(f"ticket \"{char}\" - {match_length}{match_symbol}")
            elif match_length == 10:
                print(f"ticket \"{char}\" - {match_length}{match_symbol} Jackpot!")
            else:
                print(f"ticket \"{char}\" - no match")
    else:
        print("invalid ticket")
