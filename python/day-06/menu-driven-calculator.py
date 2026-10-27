while True:
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting the calculator.")
        break

    if choice in [1, 2, 3, 4]:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))

        if choice == 1:
            result = n1 + n2
            print("Result:", result)
        elif choice == 2:
            result = n1 - n2
            print("Result:", result)
        elif choice == 3:
            result = n1 * n2
            print("Result:", result)
        elif choice == 4:
            if n2 != 0:
                result = n1 / n2
                print("Result:", result)
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")