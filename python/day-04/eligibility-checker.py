age = int(input("Enter your age: "))
has_qualification = input(
    "Do you meet the required qualification? (yes/no): "
).strip().lower()

if age < 0:
    print("Age cannot be negative.")
elif age >= 18 and has_qualification == "yes":
    print("You meet the example requirements.")
elif age < 18:
    print("You must be at least 18.")
elif has_qualification != "yes":
    print("You do not meet the qualification requirement.")