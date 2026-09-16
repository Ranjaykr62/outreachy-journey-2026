# Challenge 1 — Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Example usage
choice = input("Enter choice (+, -, *, /): ")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if choice == "+":
    print("Result:", add(x, y))
elif choice == "-":
    print("Result:", subtract(x, y))
elif choice == "*":
    print("Result:", multiply(x, y))
elif choice == "/":
    print("Result:", divide(x, y))
else:
    print("Invalid choice")
