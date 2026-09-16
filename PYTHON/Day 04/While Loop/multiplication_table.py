# Multiplication table using while loop

num = int(input("Enter a number: "))  # user input
i = 1

print(f"\nMultiplication Table of {num}")
while i <= 10:   # loop from 1 to 10
    print(f"{num} x {i} = {num * i}")
    i += 1       # increment
