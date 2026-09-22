# Count total characters in a file
with open("student.txt", "r") as f:
    text = f.read()
print("Total characters:", len(text))
