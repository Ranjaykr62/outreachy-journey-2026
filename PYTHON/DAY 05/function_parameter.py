# function_parameters.py

# 1. Function that takes a name and prints a greeting
def greet(name):
    print(f"Hello, {name}!")

# 2. Function that takes two numbers and prints their sum
def add_numbers(a, b):
    print("Sum:", a + b)

# 3. Function that takes a number and prints its multiplication table
def multiplication_table(num):
    print(f"\nMultiplication Table of {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# 4. Function that takes a number and checks whether it is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# 5. Function that takes a number and prints its square
def print_square(num):
    print(f"Square of {num} is {num * num}")

# 6. Function that takes three numbers and prints the largest
def largest_of_three(a, b, c):
    print("Largest number is:", max(a, b, c))

# 7. Function with a default parameter for a greeting
def custom_greet(name="Friend"):
    print(f"Hello, {name}! Welcome to Python.")


# -------------------------
# Example calls to test them
# -------------------------
greet("Ranjay")
add_numbers(10, 20)
multiplication_table(5)
check_even_odd(7)
print_square(9)
largest_of_three(12, 45, 33)
custom_greet()          # uses default
custom_greet("Ranjay")  # custom name
