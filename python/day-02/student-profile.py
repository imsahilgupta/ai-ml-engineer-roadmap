# Store student information
student_name = input("Enter your name: ")
education = input("Enter your education: ")
career_goal = input("Enter your career goal: ")
study_hours = float(input("Hours studied today: "))

# Display a formatted profile
print("\n--- Student Profile ---")
print(f"Name: {student_name}")
print(f"Education: {education}")
print(f"Career goal: {career_goal}")
print(f"Study hours today: {study_hours:.1f}")

# Display data types
print("\n--- Data Types ---")
print(f"student_name: {type(student_name).__name__}")
print(f"education: {type(education).__name__}")
print(f"career_goal: {type(career_goal).__name__}")
print(f"study_hours: {type(study_hours).__name__}")