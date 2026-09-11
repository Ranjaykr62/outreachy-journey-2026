# Dictionary of students and their marks
students = {
    "Ranjay": 85,
    "Amit": 92,
    "Sneha": 78,
    "Rahul": 88
}

# Find student with highest marks
top_student = max(students, key=students.get)

print("Student with highest marks:", top_student)
print("Marks:", students[top_student])


# Dictionary with subject marks
students = {
    "Ranjay": {"Python": 85, "Math": 90, "English": 78},
    "Amit": {"Python": 92, "Math": 88, "English": 80},
    "Sneha": {"Python": 75, "Math": 95, "English": 85}
}

# Calculate total marks for each student
totals = {name: sum(marks.values()) for name, marks in students.items()}

# Find student with highest total
top_student = max(totals, key=totals.get)

print("Student with highest total marks:", top_student)
print("Total Marks:", totals[top_student])
