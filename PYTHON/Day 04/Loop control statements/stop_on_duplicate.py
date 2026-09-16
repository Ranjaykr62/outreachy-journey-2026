seen = set()

while True:
    num = int(input("Enter a number (duplicate to stop): "))
    if num in seen:
        print("Duplicate entered! Loop stopped.")
        break
    seen.add(num)
    print("You entered:", num)
