# Challenge 4 — Menu-Driven Program

def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def reverse_number(num):
    return int(str(num)[::-1])

while True:
    print("\nMenu:")
    print("1. Check Even/Odd")
    print("2. Check Prime")
    print("3. Find Factorial")
    print("4. Reverse Number")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Exiting program...")
        break

    num = int(input("Enter a number: "))

    if choice == 1:
        print(check_even_odd(num))
    elif choice == 2:
        print("Prime?" , is_prime(num))
    elif choice == 3:
        print("Factorial:", factorial(num))
    elif choice == 4:
        print("Reverse:", reverse_number(num))
    else:
        print("Invalid choice")
