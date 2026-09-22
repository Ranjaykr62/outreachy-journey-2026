# File Word Analyzer
filename = input("Enter file name: ")

with open(filename, "r") as f:
    text = f.read()

lines = text.splitlines()
words = text.split()
characters = len(text)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)
