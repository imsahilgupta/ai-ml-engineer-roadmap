"""
Exercise 3 — Common interests
Given two sets of interests, print their union, intersection, and difference.
person_a = {"coding", "music", "reading"}
person_b = {"music", "travel", "coding"}
Challenge: find interests that only one person has.
"""

person_a = {"coding", "music", "reading"}
person_b = {"music", "travel", "coding"}

# Find common interests using set intersection
print("Unique interests of person A and person B:", person_a | person_b)
print("Intersection interests of person A and person B:", person_a & person_b)
print("Difference interests of person A and person B:", person_a - person_b)

# Challenge: Find interests that only one person has using set symmetric difference
print("Interests that only one person has:", person_a ^ person_b)