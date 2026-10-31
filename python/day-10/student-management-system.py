students = {}

def add_student():
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        marks = float(input("Enter student marks: "))
    except ValueError:
        print("Marks must be numeric.")
        return

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully.")

def view_students():
    if not students:
        print("No student records found.")
        return

    for student_id, details in students.items():
        print(
            f"ID: {student_id} | "
            f"Name: {details['name']} | "
            f"Marks: {details['marks']}"
        )

def search_student():
    student_id = input("Enter student ID: ").strip()

    student = students.get(student_id)

    if student is None:
        print("Student not found.")
        return

    print("Name:", student["name"])
    print("Marks:", student["marks"])

def update_marks():
    student_id = input("Enter student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    try:
        marks = float(input("Enter new marks: "))
    except ValueError:
        print("Marks must be numeric.")
        return

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    students[student_id]["marks"] = marks
    print("Marks updated successfully.")

def delete_student():
    student_id = input("Enter student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    del students[student_id]
    print("Student deleted successfully.")

def calculate_average():
    if not students:
        print("No records available.")
        return

    marks = [
        details["marks"]
        for details in students.values()
    ]

    average = sum(marks) / len(marks)
    print(f"Class average: {average:.2f}")

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Update marks")
        print("5. Delete student")
        print("6. Calculate class average")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()