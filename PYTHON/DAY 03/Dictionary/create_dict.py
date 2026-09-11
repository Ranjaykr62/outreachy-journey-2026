# Create a dictionary for student info
student = {
    "Name": "Ranjay Kumar",
    "Age": 21,
    "College": "IIT Patna",
    "Python Marks": 85,
    "Mathematics Marks": 90,
    "English Marks": 78,
    "Physics Marks": 88
}

# Print the dictionary
print("Student Information Dictionary:")
print(student)

# Print each key-value pair clearly
print("\n--- Detailed Info ---")
for key, value in student.items():
    print(key, ":", value)


# Create dictionary from user input
student = {
    "Name": input("Enter your name: "),
    "Age": int(input("Enter your age: ")),
    "College": input("Enter your college: "),
    "Python Marks": float(input("Enter Python marks: ")),
    "Mathematics Marks": float(input("Enter Mathematics marks: ")),
    "English Marks": float(input("Enter English marks: ")),
    "Physics Marks": float(input("Enter Physics marks: "))
}

print("\n--- Student Info ---")
for key, value in student.items():
    print(key, ":", value)
