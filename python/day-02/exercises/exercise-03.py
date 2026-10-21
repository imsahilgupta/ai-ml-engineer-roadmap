# Ask two numbers from the user
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

# Convert the input to floats
number1 = float(number1)
number2 = float(number2)

# Perform arithmetic operations
sum_result = number1 + number2
difference_result = number1 - number2
product_result = number1 * number2
quotient_result = number1 / number2 if number2 != 0 else "Undefined (division by zero)"

# Display their sum, difference, product, and quotient
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")