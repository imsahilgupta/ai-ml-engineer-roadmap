"""
Exercise 3 — Shopping bill calculator
File: exercises/exercise-03.py

Ask the user for an item's price and quantity. Calculate the subtotal, apply a 10% discount if the subtotal is at least 1,000, and print the final amount.

Requirements: use float() or int() as appropriate, arithmetic operators, comparison operators, and a conditional statement. If you haven't learned conditionals yet, use the calculator example as a guide and ask for help if needed.
"""

# ask the user for the item's price and quantity
item_price = float(input("Enter the item's price: "))
item_quantity = int(input("Enter the item's quantity: "))

# calculate the subtotal
subtotal = item_price * item_quantity

# apply a 10% discount if the subtotal is at least 1,000
if subtotal >= 1000:
    discount = subtotal * 0.10
    final_amount = subtotal - discount
else:
    final_amount = subtotal

# print the final amount
print(f"The final amount is: {final_amount:.2f}")