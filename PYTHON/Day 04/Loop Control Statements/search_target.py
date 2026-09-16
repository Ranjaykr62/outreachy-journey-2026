numbers = [10, 20, 30, 40, 50]
target = 25

found = False
for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Target found:", target)
else:
    print("Target not found")
