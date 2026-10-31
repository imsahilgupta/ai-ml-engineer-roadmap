"""
Exercise 5 — Variable arguments
Write a function using *args that accepts any number of numerical values and returns their sum.
Challenge: return the average too, while safely handling zero arguments.
"""

def analyze_args(*args):
    # Challenge: Handle zero arguments safely
    if not args:
        return {
            "sum": 0,
            "average": None
        }
    
    total = sum(args)
    average = total / len(args)
    
    return {
        "sum": total,
        "average": average
    }

# 1. Multiple numbers
print("Arguments (10, 20, 30, 40):")
print(analyze_args(10, 20, 30, 40))

# 2. Single number
print("\nArgument (5):")
print(analyze_args(5))

# 3. Zero arguments (Safely handled)
print("\nNo arguments passed:")
print(analyze_args())