"""
Exercise 2 — Exam result
Ask for a score from 0 to 100. Reject invalid scores. For valid scores, display Pass if the score is at least 40 and Fail otherwise.
"""

# ask the user for a score
score = int(input("Enter your score (0-100): "))

# check if the score is valid
if score < 0 or score > 100:
    print("Invalid score. Enter a value from 0 to 100.")
else:
    # check if the score is at least 40
    if score >= 40:
        print("Pass")
    else:
        print("Fail")