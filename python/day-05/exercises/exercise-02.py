"""
Exercise 2 — Factorial calculator
Ask the user for a non-negative integer \(n\). Calculate its factorial using a loop. For example, \(5! = 5 \times 4 \times 3 \times 2 \times 1 = 120\). Remember that \(0! = 1\).
"""

# ask the user for a non-negative integer
n = int(input("Enter a non-negative integer: "))

# calculate the factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# print the result
print(f"{n}! = {factorial}")