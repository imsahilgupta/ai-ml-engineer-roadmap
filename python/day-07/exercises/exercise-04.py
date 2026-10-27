"""
Exercise 4 — Reverse a list
Reverse a list in three ways: using slicing, using reverse(), and by building a new list with a loop. Observe which approaches modify the original list.
"""

# Create a list of integers
numbers = [1, 2, 3, 4, 5]

# Method 1: Using slicing (creates a new list)
reversed_numbers_1 = numbers[::-1]

# Method 2: Using reverse() (modifies the original list)
numbers_copy = numbers.copy()
numbers_copy.reverse()
reversed_numbers_2 = numbers_copy

# Method 3: Building a new list with a loop (creates a new list)
reversed_numbers_3 = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers_3.append(numbers[i])

print("Original list:", numbers)
print("Reversed using slicing:", reversed_numbers_1)
print("Reversed using reverse():", reversed_numbers_2)
print("Reversed using loop:", reversed_numbers_3)