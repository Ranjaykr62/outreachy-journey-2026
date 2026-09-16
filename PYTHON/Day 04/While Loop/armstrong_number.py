# Check if a number is an Armstrong number using while loop

num = int(input("Enter a number: "))  # user input
n = abs(num)   # handle negative numbers
temp = n
sum_of_powers = 0

# Count digits first
count = 0
t = n
while t > 0:
    t //= 10
    count += 1

# Calculate sum of digits raised to 'count'
while n > 0:
    digit = n % 10
    sum_of_powers += digit ** count
    n //= 10

# Compare with original number
if sum_of_powers == temp:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
