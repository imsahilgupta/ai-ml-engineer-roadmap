"""
Membership: in and not in
Membership operators check whether an item is present in a collection or substring.

Identity: is and is not
Identity operators check whether two references point to the same object, not merely whether their values are equal.
"""

# membership operators
language = "Python"

print("Py" in language)
print("Java" in language)
print("Java" not in language)


# identity operators
result = None

print(result is None)
print(result is not None)