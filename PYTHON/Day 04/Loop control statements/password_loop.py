password = "python123"

while True:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        print("Wrong password, try again.")
