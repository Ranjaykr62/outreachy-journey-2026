# Program to classify age group

age = int(input("Enter age: "))

if age < 13:
    print("Age Group: Child")
elif 13 <= age <= 19:
    print("Age Group: Teenager")
elif 20 <= age <= 35:
    print("Age Group: Young Adult")
elif 36 <= age <= 59:
    print("Age Group: Adult")
else:
    print("Age Group: Senior Citizen")
