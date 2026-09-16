# Program to check if a user input number is even or odd

num = int(input("Enter a number: "))  # user input

i = num   # start with the input number
while i <= num:   # loop runs once
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
    i += 1   # increment to exit loop
