# Program to collect student information and calculate total & average marks

# Ask for user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
college = input("Enter your college name: ")

python_marks = float(input("Enter marks in Python: "))
maths_marks = float(input("Enter marks in Mathematics: "))
english_marks = float(input("Enter marks in English: "))
physics_marks = float(input("Enter marks in Physics: "))

# Calculate total and average
total = python_marks + maths_marks + english_marks + physics_marks
average = total / 4

# Print results
print("\n--- Student Information ---")
print("Name:", name)
print("Age:", age)
print("College:", college)

print("\n--- Marks Summary ---")
print("Python:", python_marks)
print("Mathematics:", maths_marks)
print("English:", english_marks)
print("Physics:", physics_marks)
print("Total Marks:", total)
print("Average Marks:", average)
