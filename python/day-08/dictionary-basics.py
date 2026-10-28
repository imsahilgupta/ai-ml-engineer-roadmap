student = {
    "name": "Alex",
    "age": 21,
    "degree": "BCA",
    "skills": ["Python", "Git"]
}

# Read values
print(student["name"])
print(student.get("age"))
print(student.get("city", "Not provided"))

# Add and update
student["city"] = "Kathmandu"
student["age"] = 22

# Check keys
if "email" in student:
    print(student["email"])
else:
    print("Email is not available")

# Iterate through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Remove a key and retrieve its value
removed_city = student.pop("city")
print("Removed city:", removed_city)

print("Final student record:", student)
