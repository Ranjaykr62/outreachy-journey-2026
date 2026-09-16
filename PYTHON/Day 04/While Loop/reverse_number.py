# Reverse a number using while loop

num = int(input("Enter a number: "))  # user input
rev = 0
n = abs(num)   # handle negative numbers

while n > 0:
    digit = n % 10        # extract last digit
    rev = rev * 10 + digit  # build reversed number
    n //= 10              # remove last digit

# If original number was negative, make reversed negative
if num < 0:
    rev = -rev

print("Reversed number =", rev)
