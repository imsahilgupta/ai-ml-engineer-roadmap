n = int(input("Enter an integer: "))

if n < 2:
    print("Not prime")
else:
    is_prime = True

    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")