"""
Exercise 2 — Remove duplicates
Given [1, 2, 2, 3, 4, 4, 5, 1], create a new list with duplicate values removed while preserving the original order. Try doing it with a loop and membership checks.
"""

# Create a list with duplicates
original_list = [1, 2, 2, 3, 4, 4, 5, 1]

# Create a new list with duplicates removed
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original list:", original_list)
print("List with duplicates removed:", unique_list)