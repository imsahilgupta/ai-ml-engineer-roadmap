"""
Exercise 2 — Maximum of three numbers
Write a function that accepts three numbers and returns the largest one.
Challenge: solve it without using Python's built-in max().
"""

# function to find maximum number
def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(f"Max of (10, 25, 15): {find_maximum(10, 25, 15)}")  
print(f"Max of (50, 30, 20): {find_maximum(50, 30, 20)}")  
print(f"Max of (5, 5, 42): {find_maximum(5, 5, 42)}")    
print(f"Max of (-3, -7, -1): {find_maximum(-3, -7, -1)}")