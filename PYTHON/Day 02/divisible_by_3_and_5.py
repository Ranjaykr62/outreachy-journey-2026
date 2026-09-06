# Program to check divisibility by 3 and 5

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5.")
elif num % 3 == 0:
    print("The number is divisible by 3 only.")
elif num % 5 == 0:
    print("The number is divisible by 5 only.")
else:
    print("The number is not divisible by 3 or 5.")
