# Expense Tracker
with open("expenses.txt", "a") as f:
    while True:
        item = input("Enter expense item: ")
        amount = input("Enter amount: ")
        f.write(f"{item} - {amount}\n")

        choice = input("Add another expense? (y/n): ")
        if choice.lower() != "y":
            break

print("\nSaved Expenses:")
with open("expenses.txt", "r") as f:
    print(f.read())
