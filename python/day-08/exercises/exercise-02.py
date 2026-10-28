"""
Exercise 2 — Remove duplicates
Given numbers = [4, 2, 4, 7, 2, 9, 7, 1], create a collection of unique numbers and print the number of unique values.
"""

# Given list of numbers
numbers = [4, 2, 4, 7, 2, 9, 7, 1]
# Create a collection of unique numbers using a set
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)
print("Number of unique values:", len(unique_numbers))