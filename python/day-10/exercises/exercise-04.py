"""
Exercise 4 — List statistics
Write a function that accepts a list of numbers and returns its total, average, maximum, and minimum.
Challenge: handle an empty list safely. Consider returning None or a clear error result.
"""

# function
def calculate_stats(numbers):
    # Challenge: Handle empty list safely
    if not numbers:
        return {
            "total": None,
            "average": None,
            "maximum": None,
            "minimum": None
        }
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return {
        "total": total,
        "average": average,
        "maximum": maximum,
        "minimum": minimum
    }

# 1. Normal list of numbers
nums1 = [10, 25, 5, 40, 20]
print(f"Stats for {nums1}:")
print(calculate_stats(nums1))

# 2. List with negative numbers
nums2 = [-3, 12, 0, -8, 15]
print(f"\nStats for {nums2}:")
print(calculate_stats(nums2))

# 3. Empty list test (Safely handled)
empty_list = []
print(f"\nStats for empty list {empty_list}:")
print(calculate_stats(empty_list))