## Handle invalid input

try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)

except ValueError:
    print("Please enter a valid number.")



## Division by zero

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2
    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


## Multiple exceptions

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numbers only.")

except ZeroDivisionError:
    print("The second number cannot be zero.")


## Using  else

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Valid number:", number)


## Using finally

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program execution completed.")

