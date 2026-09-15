while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative number entered. Loop stopped.")
        break
    print("You entered:", num)
