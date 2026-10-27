"""
Exercise 2 — Reverse digits
Ask for a non-negative integer and reverse its digits using arithmetic and a while loop. For example, 1234 should become 4321.
"""

n = int(input("Enter a non-negative integer: "))

reversed_n = 0
while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n //= 10

print("Reversed number:", reversed_n)