# Program to check login credentials

# Predefined correct credentials
correct_username = "admin"
correct_password = "12345"

# Take input from user
username = input("Enter username: ")
password = input("Enter password: ")

# Check credentials
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password.")
