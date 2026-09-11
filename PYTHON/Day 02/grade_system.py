# Program to calculate grade based on marks

marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"

print("Marks:", marks)
print("Grade:", grade)
