# Program to check which number is greater

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("The first number is greater:", a)
elif b > a:
    print("The second number is greater:", b)
else:
    print("Both numbers are equal.")
