"""
Exercise 6 — Student grade report
Given a dictionary of student names and scores, use a dictionary comprehension to produce a second dictionary where each name maps to "Pass" or "Fail" using a threshold of 40.
Challenge: create a separate dictionary containing only students who passed, then calculate their average score. Handle the case where nobody passes.
"""

# Dictionary of student names and scores
students_scores = {
    "Alice": 85,
    "Bob": 35,
    "Charlie": 75,
    "David": 45,
    "Eve": 95
}

# Dictionary with pass/fail status
pass_fail = {name: "Pass" if score >= 40 else "Fail" for name, score in students_scores.items()}

# Dictionary containing only students who passed
passed_students = {name: score for name, score in students_scores.items() if score >= 40}

# Calculate average score of passed students
if passed_students:
    average_score = sum(passed_students.values()) / len(passed_students)
else:
    average_score = 0

print("Pass/Fail Status:", pass_fail)
print("Passed Students:", passed_students)
print("Average Score of Passed Students:", average_score)