# function_return.py

# 1. Function that returns the sum of two numbers
def add_numbers(a, b):
    return a + b

# 2. Function that returns the square of a number
def square(num):
    return num * num

# 3. Function that returns the largest of two numbers
def largest(a, b):
    return a if a > b else b

# 4. Function that returns whether a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# 5. Function that returns the factorial of a number
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# 6. Function that returns the sum of digits of a number
def sum_of_digits(num):
    total = 0
    for digit in str(abs(num)):  # abs handles negative numbers
        total += int(digit)
    return total

# 7. Function that returns both the sum and product of two numbers
def sum_and_product(a, b):
    return a + b, a * b   # returns a tuple (sum, product)


# -------------------------
# Example calls to test them
# -------------------------
print("Sum:", add_numbers(10, 20))
print("Square:", square(7))
print("Largest:", largest(15, 25))
print("Check number:", check_number(-5))
print("Factorial:", factorial(5))
print("Sum of digits:", sum_of_digits(1234))
s, p = sum_and_product(4, 6)
print("Sum:", s, "Product:", p)
