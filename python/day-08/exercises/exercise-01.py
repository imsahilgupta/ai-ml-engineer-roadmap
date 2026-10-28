"""
Exercise 1 — Tuple unpacking
Create a tuple containing a person's name, age, and city. Unpack it into three variables and print a sentence using all three.
Challenge: swap two variables using tuple unpacking.
"""

# Create a tuple with name, age, and city
person_info = ("Alice", 30, "New York")

# Unpack the tuple into three variables
name, age, city = person_info

# Print a sentence using all three variables
print(f"{name} is {age} years old and lives in {city}.")

# Challenge: swap two variables using tuple unpacking
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")

a, b = b, a
print(f"After swapping: a = {a}, b = {b}")