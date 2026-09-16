# Find second largest number in a list using loop
numbers = [12, 45, 7, 89, 34, 22]

largest = second_largest = float('-inf')  # start with very small values

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest number =", largest)
print("Second largest number =", second_largest)
