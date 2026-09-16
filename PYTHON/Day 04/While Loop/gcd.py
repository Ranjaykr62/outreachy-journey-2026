# Find GCD of two numbers using while loop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Euclidean algorithm with while loop
while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD =", a)
