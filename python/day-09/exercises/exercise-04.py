"""
Exercise 4 — Dictionary transformation
Given a dictionary of product names and prices, create a new dictionary containing only products costing more than 100.
Challenge: create another dictionary with a 15% discount applied to every qualifying product.
"""

# Dictionary of products and prices
products = {
    "laptop": 1200,
    "mouse": 25,
    "keyboard": 100,
    "monitor": 300,
    "headphones": 150
}

# Dictionary of products costing more than 100
expensive_products = {name: price for name, price in products.items() if price > 100}

# Dictionary with 15% discount applied to qualifying products
discounted_products = {name: price * 0.85 for name, price in products.items() if price > 100}

print("Expensive products:", expensive_products)
print("Discounted products:", discounted_products)