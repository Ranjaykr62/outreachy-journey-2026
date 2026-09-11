# Simple login system

# Predefined users with passwords (dictionary)
users = {
    "admin": "12345",
    "ranjay": "abc123",
    "guest": "guest"
}

# Take input from user
username = input("Enter username: ")
password = input("Enter password: ")

# Check login conditions
if username in users:
    if users[username] == password:
        print("Login successful!")
    else:
        print("Wrong password.")
else:
    print("Username not found.")
