while True:
    print("\n--- Menu ---")
    print("1. Greet")
    print("2. Add two numbers")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Hello, welcome!")
    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)
    elif choice == 3:
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")
