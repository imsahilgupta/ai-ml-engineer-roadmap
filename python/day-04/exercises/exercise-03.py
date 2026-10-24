"""
Exercise 3 — Shopping discount
Ask for a shopping subtotal. If it is at least 1,000, apply a 10% discount; otherwise, apply no discount. Display the original subtotal, discount amount, and final total.
"""

# ask the user for the shopping subtotal
subtotal = int(input("Enter the shopping subtotal: "))

# apply a 10% discount if the subtotal is at least 1,000
if subtotal >= 1000:
    discount = subtotal * 0.10
    final_total = subtotal - discount
else:
    discount = 0
    final_total = subtotal

# display the results
print(f"Original subtotal: NPR {subtotal}")
print(f"Discount amount: NPR {discount}")
print(f"Final total: NPR {final_total}")