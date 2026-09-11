# Two class lists
class1 = ["Ranjay", "Amit", "Sneha", "Rahul"]
class2 = ["Sneha", "Rahul", "Neha", "Amit"]

# Convert lists to sets
set1 = set(class1)
set2 = set(class2)

# Find common students (intersection)
common_students = set1 & set2

print("Common students:", common_students)
