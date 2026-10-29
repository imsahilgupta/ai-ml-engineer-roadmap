
scores = {
    "Asha": 85,
    "Ram": 32,
    "Mina": 91,
    "Sita": 45,
    "Hari": 68
}

PASS_MARK = 40

# Select students who passed
passed_students = {
    name: score
    for name, score in scores.items()
    if score >= PASS_MARK
}

# Select students who need improvement
failed_students = {
    name: score
    for name, score in scores.items()
    if score < PASS_MARK
}

# Convert scores to percentages, assuming scores are out of 100
percentages = {
    name: score / 100 * 100
    for name, score in scores.items()
}

# Generate a status for every student
statuses = {
    name: "Pass" if score >= PASS_MARK else "Fail"
    for name, score in scores.items()
}

print("All scores:", scores)
print("Passed:", passed_students)
print("Failed:", failed_students)
print("Statuses:", statuses)

if scores:
    average = sum(scores.values()) / len(scores)
    print(f"Class average: {average:.2f}")
    print("Highest score:", max(scores.values()))
    print("Lowest score:", min(scores.values()))
