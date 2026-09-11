# Dictionary of students and marks
students = {
    "Ranjay": 85,
    "Amit": 92,
    "Sneha": 78,
    "Rahul": 88
}

# Find key with largest value
top_student = max(students, key=students.get)

print("Key with largest value:", top_student)
print("Largest value:", students[top_student])
