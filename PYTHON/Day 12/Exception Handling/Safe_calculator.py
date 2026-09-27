try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = number1 + number2

    elif operation == "-":
        result = number1 - number2

    elif operation == "*":
        result = number1 * number2

    elif operation == "/":
        result = number1 / number2

    else:
        print("Invalid operation.")
        result = None

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")