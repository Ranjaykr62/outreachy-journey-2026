# List with duplicate numbers
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 10]

# Empty dictionary
freq = {}

# Count frequency
for num in numbers:
    if num in freq:
        freq[num] += 1   # increase count
    else:
        freq[num] = 1    # first time, set count = 1

print(freq)
