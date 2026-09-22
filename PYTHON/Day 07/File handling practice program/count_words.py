# Count total words in a file
with open("student.txt", "r") as f:
    text = f.read()
words = text.split()
print("Total words:", len(words))
