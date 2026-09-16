# Reverse a string using for loop
text = input("Enter a string: ")
reversed_str = ""

for ch in text:
    reversed_str = ch + reversed_str   # prepend each character

print("Reversed string =", reversed_str)
