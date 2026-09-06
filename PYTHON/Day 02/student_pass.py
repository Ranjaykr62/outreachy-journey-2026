# Program to check if student passed all subjects

# Input marks for subjects
math = int(input("Enter Mathematics marks: "))
english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))

# Pass condition: at least 40 in each subject
if math >= 40 and english >= 40 and science >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
