"""
Exercise 1 — Number classifier
Ask the user for a number. Display whether it is positive, negative, or zero. Then display whether it is even or odd for integer input.
"""

# ask the user for a number
number = int(input("Enter a number: "))

# check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# check if the number is even or odd
if number % 2 == 0:
    print("The number is even.")   
else:
    print("The number is odd.")   