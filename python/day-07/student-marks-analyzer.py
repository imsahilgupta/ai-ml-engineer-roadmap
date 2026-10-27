marks = [78, 85, 92, 67, 88]

total = sum(marks)
average = total / len(marks)

print("Marks:", marks)
print("Number of students:", len(marks))
print("Total marks:", total)
print(f"Average marks: {average:.2f}")
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))

print("\nResults:")
for index, mark in enumerate(marks, start=1):
    if mark >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(f"Student {index}: {mark} — {result}")