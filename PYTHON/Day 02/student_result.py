# Program to calculate student result

# Input marks for 3 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Calculate total and average
total = sub1 + sub2 + sub3
average = total / 3

# Determine grade based on average
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "fail"

# Display result
print("\n--- Student Result ---")
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)