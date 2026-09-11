# List with duplicate numbers
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 10]

# Empty set to track seen numbers
seen = set()

# Empty set to store duplicates
duplicates = set()

# Loop through each number
for num in numbers:
    if num in seen:
        duplicates.add(num)   # already seen → duplicate
    else:
        seen.add(num)         # first time → add to seen

print("Duplicates:", duplicates)
