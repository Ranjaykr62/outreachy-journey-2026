# Copy contents of one file into another
with open("student.txt", "r") as f1:
    data = f1.read()

with open("student_copy.txt", "w") as f2:
    f2.write(data)

print("File copied successfully!")
