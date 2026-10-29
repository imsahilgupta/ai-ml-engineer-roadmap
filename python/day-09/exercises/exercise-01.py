"""
Exercise 1 — Squares and cubes
Given a list of integers from 1 to 10, create one list containing their squares and another containing their cubes using list comprehensions.
Challenge: include only the squares of odd numbers.
"""

# list of integers from 1 to 10
numbers = list(range(1, 11))

# List of squares
squares = [x**2 for x in numbers]

# List of cubes
cubes = [x**3 for x in numbers]

# Challenge: List of squares of odd numbers
odd_squares = [x**2 for x in numbers if x % 2 != 0]

print("Squares:", squares)
print("Cubes:", cubes)
print("Squares of odd numbers:", odd_squares)