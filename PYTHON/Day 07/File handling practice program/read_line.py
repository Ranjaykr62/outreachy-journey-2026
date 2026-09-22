# Read file line by line
with open("student.txt", "r") as f:
    for line in f:
        print(line.strip())
