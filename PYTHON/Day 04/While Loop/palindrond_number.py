# Check if a number is a palindrome using while loop

num = int(input("Enter a number: "))  # user input
n = abs(num)   # handle negative numbers
rev = 0
temp = n       # store original number

while n > 0:
    digit = n % 10          # extract last digit
    rev = rev * 10 + digit  # build reversed number
    n //= 10                # remove last digit

# Compare original with reversed
if temp == rev:
    print(num, "is a Palindrome")
else:
    print(num, "is Not a Palindrome")

