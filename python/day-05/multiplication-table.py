number = int(input("Enter a number: "))

print(f"\nMultiplication table for {number}")

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")