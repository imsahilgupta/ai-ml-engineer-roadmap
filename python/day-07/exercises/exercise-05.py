"""
Exercise 5 — Search for an element
Ask the user for a number and search for it in a list. Display its index if found, or a helpful message if it is absent. If the value appears multiple times, try displaying every matching index.
"""

# Create a list of integers
numbers = [12, 7, 9, 15, 22, 5, 18, 11, 30, 4]

# Ask the user for a number
user_input = int(input("Enter a number to search for: "))

# Search for the number in the list
indices = []
for i, num in enumerate(numbers):
    if num == user_input:
        indices.append(i)

# Display the results
if indices:
    print(f"The number {user_input} was found at index(es): {indices}")
else:
    print(f"The number {user_input} was not found in the list.")