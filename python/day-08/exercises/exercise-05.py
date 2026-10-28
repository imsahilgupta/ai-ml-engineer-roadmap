"""
Exercise 5 — Marks analysis
Given a dictionary of student names and marks, calculate the average, highest score, lowest score, and number of students who passed using 40 as the practice threshold.
Challenge: handle an empty dictionary without dividing by zero.
"""

# Create a dictionary of student names and marks
marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 96,
    "Eve": 88
}

# Calculate average, highest score, lowest score, and number of students who passed
if marks:
    average_score = sum(marks.values()) / len(marks)
    highest_score = max(marks.values())
    lowest_score = min(marks.values())
    passed_students = sum(1 for score in marks.values() if score >= 40)

    print(f"Average Score: {average_score:.2f}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Number of Students Passed: {passed_students}")
else:
    print("No student marks available.")

# Challenge: handle an empty dictionary without dividing by zero
if not marks:
    print("No student marks available to analyze.")