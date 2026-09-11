# Program to calculate average marks of four subjects

# Ask for user input
python_marks = float(input("Enter marks in Python: "))
maths_marks = float(input("Enter marks in Maths: "))
english_marks = float(input("Enter marks in English: "))
physics_marks = float(input("Enter marks in Physics: "))

# Calculate total and average
total = python_marks + maths_marks + english_marks + physics_marks
average = total / 4

# Print results
print("\n--- Marks Summary ---")
print("Python:", python_marks)
print("Maths:", maths_marks)
print("English:", english_marks)
print("Physics:", physics_marks)
print("Total Marks:", total)
print("Average Marks:", average)
