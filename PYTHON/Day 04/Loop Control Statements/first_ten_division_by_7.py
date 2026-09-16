count = 0
num = 1

print("First 10 numbers divisible by 7:")

while count < 10:
    if num % 7 == 0:
        print(num)
        count += 1
    num += 1
