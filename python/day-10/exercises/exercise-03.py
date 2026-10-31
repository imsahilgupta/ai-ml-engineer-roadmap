"""
Exercise 3 — Factorial function
Write factorial(number) using a loop. Return the factorial of a non-negative integer.
Test 0, 1, 5, and a negative input. Decide how your function should handle invalid values.
"""

# factorial function
def factorial(number):
    # Handle invalid negative values
    if number < 0:
        return "Error: Factorial is not defined for negative numbers."
    
    result = 1
    # Multiply numbers from 2 up to the given number
    for i in range(2, number + 1):
        result *= i
        
    return result

print(f"Factorial of 0: {factorial(0)}")    
print(f"Factorial of 1: {factorial(1)}")   
print(f"Factorial of 5: {factorial(5)}")  
print(f"Factorial of -3: {factorial(-3)}")  