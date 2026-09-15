# Print each character of a string
text = input("Enter a string: ")

for ch in text:
    print(ch)


text = input("Enter a string: ")

for i in range(len(text)):
    print(f"Index {i} -> {text[i]}")
