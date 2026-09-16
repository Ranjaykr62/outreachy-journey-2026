# Count digits of a number

num = int(input("Enter a number: "))
count = 0

# If number is 0, it has 1 digit
if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10   # Remove last digit
        count += 1        # Increase count

print("Number of digits =", count)
