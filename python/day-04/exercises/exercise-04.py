"""
Exercise 4 — Scholarship screening practice
Ask for a student's score and attendance percentage. For this practice scenario, a student qualifies only when the score is at least 80 and attendance is at least 90%. Validate both values are within 0–100 before checking qualification.
"""

# ask the user for a score and attendance percentage
score = int(input("Enter your score (0-100): "))
attendance = int(input("Enter your attendance percentage (0-100): "))

# validate the inputs
if score < 0 or score > 100:
    print("Invalid score. Enter a value from 0 to 100.")
elif attendance < 0 or attendance > 100:
    print("Invalid attendance percentage. Enter a value from 0 to 100.")
else:
    # check if the student qualifies
    if score >= 80 and attendance >= 90:
        print("Congratulations! You qualify for the scholarship.")
    else:
        print("Sorry, you do not qualify for the scholarship.")