def validate_lenght(password):
    if len(password) <6 or len(password) >10:
        return "Password must "