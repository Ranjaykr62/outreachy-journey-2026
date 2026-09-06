# Program to classify age into categories

age = int(input("Enter age: "))

if age < 13:
    print("Category: Child")
elif 13 <= age <= 19:
    print("Category: Teenager")
elif 20 <= age <= 35:
    print("Category: Young Adult")
elif 36 <= age <= 59:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")
