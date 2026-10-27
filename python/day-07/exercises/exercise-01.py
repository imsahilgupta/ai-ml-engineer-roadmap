"""
Exercise 1 — List statistics
Create a list of at least 10 integers. Display the sum, average, minimum, maximum, and number of elements. Count how many values are even and how many are odd.
"""

# Create a list of at least 10 integers
numbers = [12, 7, 9, 15, 22, 5, 18, 11, 30, 4]

# Display statistics
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Number of elements:", len(numbers))

# Count even and odd values
even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = len(numbers) - even_count

print("Even values:", even_count)
print("Odd values:", odd_count)