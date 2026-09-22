# Read hello.txt and display contents
with open("hello.txt", "r") as f:
    content = f.read()
print("File contents:\n", content)
