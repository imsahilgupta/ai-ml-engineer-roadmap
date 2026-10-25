"""
Exercise 1 — Number sequence
Use a for loop to print numbers from 1 to 50. Then print only the even numbers from 1 to 50. Finally, calculate the sum of numbers from 1 to 50.
"""

print("\nNumbers from 1 to 50:")
for number in range(1, 51):
    print(number)

print("\nEven numbers from 1 to 50:")
for number in range(2, 51, 2):
    print(number)

print("\nSum of numbers from 1 to 50:")
total = sum(range(1, 51))
print(total)