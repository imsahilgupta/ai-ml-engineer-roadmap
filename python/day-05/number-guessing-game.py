secret_number = 7
guess = None
attempts = 0

print("Guess the secret number from 1 to 10.")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print(f"Correct! You won in {attempts} attempts.")