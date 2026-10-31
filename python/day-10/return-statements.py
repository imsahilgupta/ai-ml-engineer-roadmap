def calculate_sum(a, b):
    return a + b

def calculate_square(number):
    return number ** 2

def is_even(number):
    return number % 2 == 0

total = calculate_sum(10, 20)
square = calculate_square(5)
result = is_even(8)

print("Sum:", total)
print("Square:", square)
print("Is even?", result)

# Use one function's result inside another calculation
final_result = calculate_square(calculate_sum(2, 3))
print("Final result:", final_result)
