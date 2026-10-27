shopping_list = []

while True:
    print("\n--- Shopping List ---")
    print("1. View items")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if shopping_list:
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "2":
        item = input("Enter an item: ").strip()

        if item:
            shopping_list.append(item)
            print(f"Added: {item}")
        else:
            print("Item cannot be empty.")

    elif choice == "3":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed: {item}")
        else:
            print("Item not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose between 1 and 4.")