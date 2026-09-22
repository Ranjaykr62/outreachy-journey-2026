# Search for a word in a file
word = input("Enter word: ")

with open("student.txt", "r") as f:
    text = f.read()

if word in text:
    print(f"{word} found in the file.")
else:
    print(f"{word} not found in the file.")
