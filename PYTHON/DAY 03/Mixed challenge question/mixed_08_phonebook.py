# Create a phonebook dictionary
phonebook = {
    "Ranjay": "9876543210",
    "Amit": "9123456780",
    "Sneha": "9988776655",
    "Rahul": "9011223344"
}

# Ask user to enter a name to search
name = input("Enter the name to search: ")

# Check if name exists in phonebook
if name in phonebook:
    print("Phone number of", name, "is:", phonebook[name])
else:
    print("Sorry,", name, "not found in phonebook.")
