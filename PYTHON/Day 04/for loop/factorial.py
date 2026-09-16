# Find factorial of a number using for loop
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial of", n, "=", factorial)
