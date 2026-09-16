numbers = [2, 4, 6, 8, 10, 12, 14]
target = int(input("Enter number to search: "))

found = False
for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Target found:", target)
else:
    print("Target not found.")
