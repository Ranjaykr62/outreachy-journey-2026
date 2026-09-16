# Sum of digits of a number using while loop

num = int(input("Enter a number: "))  # user input
total = 0
n = abs(num)   # handle negative numbers

while n > 0:
    digit = n % 10      # extract last digit
    total += digit      # add digit to sum
    n //= 10            # remove last digit

print("Sum of digits =", total)
