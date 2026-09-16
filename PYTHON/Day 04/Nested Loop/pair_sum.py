numbers = [2, 4, 6, 8, 10, 12]
target = int(input("Enter target sum: "))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"Pair found: {numbers[i]} + {numbers[j]} = {target}")
