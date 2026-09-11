# Create a list of numbers
numbers = [12, 45, 7, 89, 23, 56]

# Sort the list in descending order
numbers_sorted = sorted(numbers, reverse=True)

# Get the second largest
second_largest = numbers_sorted[1]

print("Second largest number:", second_largest)




# (Using max() and remove())


# Create a list of numbers
numbers = [12, 45, 7, 89, 23, 56]


# Find the largest and remove it
largest = max(numbers)
numbers.remove(largest)

# Find the new largest (which is the second largest overall)
second_largest = max(numbers)

print("Second largest number:", second_largest)
