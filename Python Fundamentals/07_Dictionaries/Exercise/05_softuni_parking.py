num_commands = int(input())
cars_on_parking = {}

for n in range(num_commands):
    command = input().split()
    username = command[1]
    if "register" in command:
        reg_number = command[2]

        if username in cars_on_parking:
            print(f"ERROR: already registered with plate number {reg_number}")
        else:
            cars_on_parking[username] = reg_number
            print(f"{username} registered {reg_number} successfully")

    elif "unregister" in command:
        if username not in cars_on_parking:
            print(f"ERROR: user {username} not found")
        else:
            del cars_on_parking[username]
            print(f"{username} unregistered successfully")

for key, item in cars_on_parking.items():
    print(f"{key} => {item}")