# Day 12 - Debugging Practice


## Question 1 - Syntax Error

print("Hello")


## Question 2 - NameError

name = "Ranjay"
print(name)


## Question 3 - TypeError

number = int(input("Enter a number: "))
result = number + 10
print(result)


## Question 4 - IndexError

numbers = [10, 20, 30]
print(numbers[2])


## Question 5 - ZeroDivisionError

number = 10
divisor = 2

try:
    result = number / divisor
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero.")


# # Question 6 - Logical Error

for i in range(1, 11):
    print(i)


## Question 7 - Function Error

def addition(a, b):
    return a + b


number1 = 10
number2 = 20

print(addition(number1, number2))


## Question 8 - Calculator

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

result = number1 + number2

print("Result:", result)