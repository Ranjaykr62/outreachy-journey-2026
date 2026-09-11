# List with duplicates
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 10]

# Empty dictionary to count frequency
freq = {}

# Count frequency of each number
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Separate unique and duplicate elements
unique = [num for num, count in freq.items() if count == 1]
duplicates = [num for num, count in freq.items() if count > 1]

print("Unique elements:", unique)
print("Duplicate elements:", duplicates)
