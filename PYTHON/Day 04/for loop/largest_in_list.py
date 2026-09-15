# Find largest number in a list without using max()

numbers = [12, 45, 7, 89, 34, 22]
largest = numbers[0]   # assume first element is largest

for num in numbers:
    if num > largest:
        largest = num

print("Largest number in the list =", largest)
