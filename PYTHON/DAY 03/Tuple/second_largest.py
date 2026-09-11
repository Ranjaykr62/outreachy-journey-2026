# Using sorted()

# Create a tuple
numbers = (10, 25, 7, 42, 18)

# Sort the tuple in descending order
sorted_numbers = sorted(numbers, reverse=True)

# Get the second largest element
second_largest = sorted_numbers[1]

print("Tuple:", numbers)
print("Second largest element:", second_largest)
