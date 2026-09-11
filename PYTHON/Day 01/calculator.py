# Basic Calculator Program

# Ask for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = "Error! Division by zero." if num2 == 0 else num1 / num2

# Print results
print("\n--- Calculator Results ---")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
