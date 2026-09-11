# Program to check age range

age = int(input("Enter age: "))

if 0 <= age <= 12:
    print("Age Range: Child (0–12)")
elif 13 <= age <= 19:
    print("Age Range: Teenager (13–19)")
elif 20 <= age <= 35:
    print("Age Range: Young Adult (20–35)")
elif 36 <= age <= 59:
    print("Age Range: Adult (36–59)")
elif age >= 60:
    print("Age Range: Senior Citizen (60+)")
else:
    print("Invalid age entered!")
