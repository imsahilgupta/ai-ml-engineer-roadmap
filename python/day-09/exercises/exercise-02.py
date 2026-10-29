"""
Exercise 2 — Filter positive numbers
Given numbers = [-5, 0, 3, -2, 8, 10, -1], create a list containing only positive values.
Challenge: create a second list containing the squares of positive values only.
"""

# list of numbers
numbers = [-5, 0, 3, -2, 8, 10, -1]

# List of positive numbers
positive_numbers = [x for x in numbers if x > 0]

# List of squares of positive numbers
positive_squares = [x**2 for x in numbers if x > 0]

print("Positive numbers:", positive_numbers)
print("Squares of positive numbers:", positive_squares)