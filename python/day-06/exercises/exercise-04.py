"""
Exercise 4 — Marks analysis
Ask how many students' marks will be entered, then process each mark using a loop. Calculate the total, average, highest mark, and lowest mark. Assume marks must be between 0 and 100; decide how to handle invalid values.
"""
# ask for the number of students marks to be entered
num_students = int(input("Enter the number of students: "))

# initialize variables for calculations
total = 0
highest = float('-inf')
lowest = float('inf')

# process each student's mark
for _ in range(num_students):
    while True:
        try:
            mark = float(input("Enter a mark (0-100) for student {}: ".format(_ + 1)))
            if 0 <= mark <= 100:
                break
            else:
                print("Invalid mark. Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    total += mark

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

# calculate average
average = total / num_students

# display results
print("Total:", total)
print("Average:", average)
print("Highest mark:", highest)
print("Lowest mark:", lowest)