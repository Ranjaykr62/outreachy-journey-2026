# Append another line to student.txt
with open("student.txt", "a") as f:
    f.write("Goal: Open Source Contribution\n")
print("Line appended successfully!")
