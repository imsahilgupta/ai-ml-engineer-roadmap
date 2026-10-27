"""
Exercise 3 — Second-largest distinct value
Find the second-largest distinct number in a list without simply sorting the entire list. Decide what your program should do if the list has fewer than two distinct values.
"""

# Create a list of integers
numbers = [5, 3, 8, 1, 4, 8, 2, 5]

# Find the second-largest distinct value
distinct_numbers = list(set(numbers))
if len(distinct_numbers) < 2:
    print("The list does not have enough distinct values.")
else:
    distinct_numbers.sort(reverse=True)
    print("The second-largest distinct value is:", distinct_numbers[1])