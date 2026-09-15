# Sum of digits of a number

num = int(input("Enter a number: "))
total = 0

# Handle negative numbers
n = abs(num)

while n > 0:
    digit = n % 10      # extract last digit
    total += digit      # add digit to sum
    n //= 10            # remove last digit

print("Sum of digits =", total)
