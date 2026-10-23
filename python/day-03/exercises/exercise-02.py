"""
Create variables age, score, and registered. Print whether the person is at least 18, scored at least 60, and is registered. Then calculate whether all three conditions are true.

Requirements: use >=, and, and at least one other comparison operator. Test both true and false cases.
"""

# Create variables
age = int(input("Enter age: "))
score = int(input("Enter score: "))
registered = input("Is the person registered? (yes/no): ")

print("****************")

# Print whether the person is at least 18, scored at least 60, and is registered
print("Is the person at least 18?", age >= 18)
print("Did the person score at least 60?", score >= 60)
print("Is the person registered?", registered == "yes")
print("****************")
print("Are all conditions true?", age >= 18 and score >= 60 and registered == "yes")