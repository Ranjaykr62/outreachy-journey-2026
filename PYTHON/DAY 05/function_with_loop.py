# functions_with_loops.py

# 1. Function that checks whether a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 2. Function that prints all even numbers between two numbers
def print_even_numbers(start, end):
    print(f"Even numbers between {start} and {end}:")
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

# 3. Function that returns the reverse of a number
def reverse_number(num):
    return int(str(num)[::-1])

# 4. Function that checks whether a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# 5. Function that prints all factors of a number
def print_factors(num):
    print(f"Factors of {num}:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()

# 6. Function that returns the factorial of a number
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# 7. Function that prints a star triangle
def star_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

# 8. Function that prints a multiplication table
def multiplication_table(num):
    print(f"\nMultiplication Table of {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


# -------------------------
# Example calls to test them
# -------------------------
print("Is 17 prime?", is_prime(17))
print_even_numbers(1, 20)
print("Reverse of 1234:", reverse_number(1234))
print("Is 121 palindrome?", is_palindrome(121))
print_factors(36)
print("Factorial of 5:", factorial(5))
star_triangle(5)
multiplication_table(7)
