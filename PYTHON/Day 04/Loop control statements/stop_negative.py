while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        print("Loop stopped because you entered a negative number.")
        break
    print("You entered:", num)
