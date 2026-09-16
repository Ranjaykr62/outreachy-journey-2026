# function_basics.py

# 1. Function to print "Hello, Python!"
def say_hello():
    print("Hello, Python!")

# 2. Function to print your name
def print_name():
    print("Ranjay Kumar")

# 3. Function to print your learning goal
def print_goal():
    print("My goal is to master Computer Science and become excellent in DSA, AI, and freelancing.")

# 4. Function to print numbers from 1 to 10
def print_numbers():
    for i in range(1, 11):
        print(i)

# 5. Function to print a multiplication table of a given number
def multiplication_table(num):
    print(f"\nMultiplication Table of {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

