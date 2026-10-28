numbers = {1, 2, 2, 3, 3, 4}

print("Unique numbers:", numbers)
print("Number of unique values:", len(numbers))

# Add and remove
numbers.add(5)
numbers.discard(2)  # Safe if 2 is absent

print("After changes:", numbers)

# Membership
print("Is 3 present?", 3 in numbers)

# Set operations
python_students = {"Asha", "Ram", "Mina"}
ml_students = {"Mina", "Sita", "Ram"}

print("In either group:", python_students | ml_students)
print("In both groups:", python_students & ml_students)
print("Only in Python group:", python_students - ml_students)
print("Different between groups:", python_students ^ ml_students)

# Remove duplicate names from a list
names = ["Asha", "Ram", "Asha", "Mina", "Ram"]
unique_names = set(names)

print("Unique names:", unique_names)
