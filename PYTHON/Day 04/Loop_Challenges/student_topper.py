marks = {"Ravi": 85, "Anita": 92, "Karan": 78, "Meena": 95}
topper = None
highest = 0

for student in marks:
    if marks[student] > highest:
        highest = marks[student]
        topper = student

print("Topper is", topper, "with marks", highest)
