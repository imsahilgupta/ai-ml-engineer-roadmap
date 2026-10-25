"""
Exercise 4 — Pattern printer
Use nested loops to print this pattern:
*
**
***
****
*****
Challenge: Print the same pattern upside down.
"""

# print the pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()