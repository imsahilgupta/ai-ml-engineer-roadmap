students = {
    "S001": {"name": "Asha", "marks": 85},
    "S002": {"name": "Ram", "marks": 72},
    "S003": {"name": "Mina", "marks": 91}
}

# Display all students
for student_id, details in students.items():
    print(
        f"ID: {student_id} | "
        f"Name: {details['name']} | "
        f"Marks: {details['marks']}"
    )

# Find a particular student
search_id = input("\nEnter student ID to search: ").strip().upper()

if search_id in students:
    details = students[search_id]
    print("Student found:", details["name"])
    print("Marks:", details["marks"])
else:
    print("Student ID not found.")

# Calculate the average mark
if students:
    marks = [details["marks"] for details in students.values()]
    average = sum(marks) / len(marks)
    print(f"Average marks: {average:.2f}")
