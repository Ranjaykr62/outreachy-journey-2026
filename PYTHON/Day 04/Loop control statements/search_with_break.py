numbers = [2, 4, 6, 8, 10, 12, 14]
search = int(input("Enter number to search: "))

for num in numbers:
    if num == search:
        print("Found:", num)
        break
