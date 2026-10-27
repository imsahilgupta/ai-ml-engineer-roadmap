"""
Exercise 1 — Even and odd statistics
Ask for a positive integer n. From 1 to n, count the even numbers, count the odd numbers, and calculate their separate sums.
"""

n = int(input("Enter a positive integer: "))

even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_count += 1
        even_sum += i
    else:
        odd_count += 1
        odd_sum += i

print("Even numbers:")
print("Count:", even_count)
print("Sum:", even_sum)

print("Odd numbers:")
print("Count:", odd_count)
print("Sum:", odd_sum)