n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter an integer greater than zero.")
else:
    total = 0

    for number in range(1, n + 1):
        total += number

    average = total / n

    print("Sum:", total)
    print("Average:", average)