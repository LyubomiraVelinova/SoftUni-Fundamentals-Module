def perform_operation(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "divide":
        return int(a / b)
    elif operation == "multiply":
        return a * b


operation = input()
a = int(input())
b = int(input())
print(perform_operation(a,b,operation))