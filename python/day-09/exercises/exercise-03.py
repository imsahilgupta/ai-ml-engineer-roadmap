"""
Exercise 3 — Unique word lengths
File: exercise-03.py
Given words = ["python", "AI", "coding", "AI", "data", "python"], create a set of the unique word lengths.
Challenge: create a set containing only the lengths greater than 3.
"""

# given list of words
words = ["python", "AI", "coding", "AI", "data", "python"]

# Set of unique word lengths
unique_lengths = {len(word) for word in words}

# Set of lengths greater than 3
lengths_greater_than_3 = {len(word) for word in words if len(word) > 3}

print("Unique word lengths:", unique_lengths)
print("Lengths greater than 3:", lengths_greater_than_3)