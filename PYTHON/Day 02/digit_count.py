# Program to check digit count of a number

num = int(input("Enter a number: "))

digits = len(str(abs(num)))   # count digits ignoring sign

if digits == 1:
    print("The number has 1 digit.")
elif digits == 2:
    print("The number has 2 digits.")
elif digits == 3:
    print("The number has 3 digits.")
else:
    print("The number has more than 3 digits.")
