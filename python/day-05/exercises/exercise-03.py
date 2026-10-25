"""
Exercise 3 — Input until zero
Use a while loop to ask the user for numbers until they enter 0. When the loop ends, display how many non-zero numbers were entered and their sum. Do not include the terminating zero in the count.
"""

# ask the user for numbers until they enter 0
count = 0
total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    count += 1
    total += number

print(f"Number of non-zero numbers entered: {count}")
print(f"Sum of non-zero numbers: {total}")