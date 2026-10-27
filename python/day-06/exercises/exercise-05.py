"""
Exercise 5 — Number guessing without repetition
Print all numbers from 1 to 100 that are divisible by both 3 and 5. Then modify the program to print Fizz for multiples of 3, Buzz for multiples of 5, and FizzBuzz for multiples of both.
Important: Check divisibility by both 3 and 5 before checking either condition individually.
"""

# Print numbers from 1 to 100 that are divisible by both 3 and 5
print("Numbers from 1 to 100 that are divisible by both 3 and 5:")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number)

# Modify the program to print Fizz, Buzz, or FizzBuzz
print("\nFizzBuzz sequence:")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)