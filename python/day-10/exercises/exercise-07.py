"""
Exercise 7 — Prime number function
File: exercise-07.py
Write is_prime(number) that returns True for prime numbers and False otherwise.
Challenge: improve your implementation so it checks divisors only up to the square root of the number.
"""

def is_prime(number):
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False
    
    # 2 is the only even prime number
    if number == 2:
        return True
    
    # Quick filter: eliminate other even numbers right away
    if number % 2 == 0:
        return False
    
    # Challenge optimization: Check odd divisors up to the square root (number ** 0.5)
    # We step by 2 (3, 5, 7...) since we already eliminated even numbers
    max_divisor = int(number ** 0.5)
    for i in range(3, max_divisor + 1, 2):
        if number % i == 0:
            return False
            
        return True

print(f"Is 2 prime? {is_prime(2)}")     
print(f"Is 11 prime? {is_prime(11)}")   
print(f"Is 25 prime? {is_prime(25)}")    
print(f"Is 97 prime? {is_prime(97)}")     
print(f"Is 1 prime? {is_prime(1)}")       
print(f"Is -5 prime? {is_prime(-5)}")    