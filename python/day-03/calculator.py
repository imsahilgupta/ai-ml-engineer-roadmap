first_number = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        result = None
        print("Error: division by zero is not allowed.")
    else:
        result = first_number / second_number
else:
    result = None
    print("Unsupported operator.")

if result is not None:
    print(f"Result: {result}")