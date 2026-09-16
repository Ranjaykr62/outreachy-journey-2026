# Sum of first n natural numbers using while loop

n = int(input("Enter a number: "))  # user input
i = 1
total = 0

while i <= n:
    total += i   # add current number
    i += 1       # move to next number

print("Sum of numbers from 1 to", n, "=", total)
