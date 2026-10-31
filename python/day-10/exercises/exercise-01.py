"""
Exercise 1 — Even or odd function
Write a function check_even(number) that returns True if the number is even and False otherwise.
Test it with positive numbers, zero, and negative numbers.
"""

# function to check
def check_even(number):
    return number % 2 == 0

# 1. Positive numbers
print(f"Is 4 even? {check_even(4)}")   
print(f"Is 7 even? {check_even(7)}")    

# 2. Zero
print(f"Is 0 even? {check_even(0)}")    

# 3. Negative numbers
print(f"Is -2 even? {check_even(-2)}")  
print(f"Is -5 even? {check_even(-5)}")  