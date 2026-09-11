numbers = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

print("Duplicate elements:", duplicates)

