# Keep taking input until user enters 0

num = int(input("Enter a number (0 to stop): "))

while num != 0:   # loop continues until 0 is entered
    print("You entered:", num)
    num = int(input("Enter a number (0 to stop): "))

print("Loop ended because you entered 0.")
