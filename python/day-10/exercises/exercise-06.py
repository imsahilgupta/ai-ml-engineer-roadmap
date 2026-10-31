"""
Exercise 6 — Student profile
Write a function using **kwargs to accept student details and print them as key-value pairs.
Challenge: require a name field and display a default message if city is not supplied.
"""

def student_profile(**kwargs):
    # Challenge 1: Require a name field
    if "name" not in kwargs:
        return "Error: A 'name' field is required to generate a profile."
    
    print("--- Student Profile ---")
    
    # Challenge 2: Handle default message if city is not supplied
    if "city" not in kwargs:
        kwargs["city"] = "Not specified (Default: Remote / Unknown)"
    
    # Print each key-value pair dynamically
    for key, value in kwargs.items():
        # Format keys nicely (e.g., student_id -> Student Id)
        formatted_key = key.replace("_", " ").title()
        print(f"{formatted_key}: {value}")
        
    print("-" * 25)

# 1. Providing all details including name and city
student_profile(name="Alice Smith", age=21, city="New York", course="Computer Science")

print("\n")

# 2. Omitting the city (triggers the default message)
student_profile(name="Bob Jones", age=23, course="Data Science", gpa=3.8)

print("\n")

# 3. Omitting the required name field (triggers error message)
print(student_profile(age=25, city="London", course="Web Development"))