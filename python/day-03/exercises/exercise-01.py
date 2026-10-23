"""
Exercise 1 — Arithmetic explorer
File: exercises/exercise-01.py

Write a program that stores two numbers and displays their sum, difference, product, division, floor division, remainder, and exponentiation.

Requirements: use variables, arithmetic operators, and descriptive output labels. Test with 17 and 5.
"""

# stores two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# displays their sum, difference, product, division, floor division, remainder, and exponentiation
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Remainder:", num1 % num2)
print("Exponentiation:", num1 ** num2)