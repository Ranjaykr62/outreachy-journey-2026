# Program to check divisibility by 2 or 3

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("The number is divisible by both 2 and 3.")
elif num % 2 == 0:
    print("The number is divisible by 2 only.")
elif num % 3 == 0:
    print("The number is divisible by 3 only.")
else:
    print("The number is not divisible by 2 or 3.")
