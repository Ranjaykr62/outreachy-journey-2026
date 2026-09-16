# Menu-driven calculator using while loop

while True:
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting calculator... Goodbye!")
        break   # exit the loop

    # For choices 1–4, take two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)
    elif choice == 2:
        print("Result =", num1 - num2)
    elif choice == 3:
        print("Result =", num1 * num2)
    elif