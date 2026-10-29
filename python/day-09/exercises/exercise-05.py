"""
Exercise 5 — Flatten a matrix
Given matrix = [[1, 2], [3, 4], [5, 6]], flatten it into a single list using a nested list comprehension.
Challenge: create a list of only the even numbers in the flattened result.
"""

# given matrix
matrix = [[1, 2], [3, 4], [5, 6]]

# flatten the matrix
flattened = [num for row in matrix for num in row]

# list of only the even numbers
even_numbers = [num for num in flattened if num % 2 == 0]

print("Flattened matrix:", flattened)
print("Even numbers:", even_numbers)