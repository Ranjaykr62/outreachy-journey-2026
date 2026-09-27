try:
    balance = float(input("Enter account balance: "))
    withdrawal = float(input("Enter withdrawal amount: "))

    if withdrawal < 0:
        print("Withdrawal cannot be negative.")

    elif withdrawal == 0:
        print("Withdrawal amount cannot be zero.")

    elif withdrawal > balance:
        print("Insufficient balance.")

    else:
        balance = balance - withdrawal
        print("Withdrawal successful.")
        print("Remaining balance:", balance)

except ValueError:
    print("Please enter valid numbers.")