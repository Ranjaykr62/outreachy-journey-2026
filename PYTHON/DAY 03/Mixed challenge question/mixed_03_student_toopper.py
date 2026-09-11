# Dictionary of students and their marks
students = {
    "Ranjay": 85,
    "Amit": 92,
    "Sneha": 78,
    "Rahul": 88
}

# Find topper using max()
topper = max(students, key=students.get)

print("Topper is:", topper)
print("Marks:", students[topper])
