# Count number of lines in a file
with open("student.txt", "r") as f:
    lines = f.readlines()
print("Total lines:", len(lines))
