# Create a tuple of 5 numbers
numbers = (10, 20, 30, 40, 50)

# Print the tuple
print("Tuple of numbers:", numbers)

# Print each element one by one
for num in numbers:
    print(num)


# Take 5 numbers from user and store in a tuple
numbers = tuple(int(input("Enter a number: ")) for i in range(5))

# Print the tuple
print("Tuple of numbers:", numbers)
