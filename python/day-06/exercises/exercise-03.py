"""
Exercise 3 — Guessing game with limited attempts
Set a secret number. Allow the user a maximum of five guesses. After each incorrect guess, tell them whether their guess is too high or too low. Stop if they guess correctly or run out of attempts.
"""

secret_number = 42
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    guess = int(input("Guess the secret number (1-100): "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

if attempts == max_attempts:
    print("Sorry, you ran out of attempts. The secret number was", secret_number)