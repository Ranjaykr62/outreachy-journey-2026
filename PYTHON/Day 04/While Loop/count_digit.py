# Count digits in a number using while loop

num = int(input("Enter a number: "))  # user input
count = 0
n = abs(num)   # handle negative numbers

while n > 0:
    n //= 10   # remove last digit
    count += 1 # increase digit count

print("The number has", count, "digits.")
