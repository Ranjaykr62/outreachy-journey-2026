# Day 11 — Reading Open-Source Code

## Project

Calculator

## Repository

Python Beginner Projects

## 1. What does this project do?

This project is a calculator that performs different mathematical operations such as addition, subtraction, multiplication, division, average, factorial, complex arithmetic, and binomial calculation.

## 2. What input does it take?

The program takes numbers from the user and asks the user to select which mathematical operation they want to perform.

## 3. What output does it produce?

The program performs the selected mathematical operation and displays the calculated result.

## 4. What files are present?

The calculator project contains:

- `main.py`

## 5. What are the function names?

The main functions are:

- addition()
- subtraction()
- multiplication()
- division()
- average()
- factorial(num)
- complex_arithmetic()
- binomial(num)

## 6. What are the parameters?

- addition() → No parameters
- subtraction() → No parameters
- multiplication() → No parameters
- division() → No parameters
- average() → No parameters
- factorial(num) → num
- complex_arithmetic() → No parameters
- binomial(num) → num

## 7. What does each function do?

- addition() — Adds multiple numbers.
- subtraction() — Subtracts the second number from the first.
- multiplication() — Multiplies multiple numbers.
- division() — Divides two numbers and checks for division by zero.
- average() — Calculates the average of multiple numbers.
- factorial(num) — Calculates the factorial of a number.
- complex_arithmetic() — Performs operations on complex numbers.
- binomial(num) — Calculates the binomial coefficient.

## 8. How does the program work from start to finish?

The program starts by displaying a menu of available operations. The user selects the operation they want to perform. The corresponding function is then called. The user enters the required numbers, and the function performs the calculation. The function returns the result, which is then displayed to the user. This process continues repeatedly until the user chooses `-1` to exit the program.

## 9. What did I learn from reading this code?

From reading this code, I learned:

1. How functions are used in a real Python project.
2. How loops are used to repeat operations.
3. How conditional statements like `if`, `elif`, and `else` control the program.
4. How arithmetic operations can be performed multiple times.
5. How `map()` can be used to convert input values into integers.
6. How one function can call another function, such as `binomial()` calling `factorial()`.

## 10. What was difficult to understand?

I found several parts of the code difficult to understand, especially `map()`, complex arithmetic, and the binomial function. I also found the repeated use of loops and functions a little difficult to understand.

## What I practiced

- Reading an open-source Python file
- Understanding functions
- Understanding parameters
- Understanding return values
- Understanding loops
- Understanding conditional statements
- Understanding `map()`
- Following the flow of a real Python program
- Reading code written by another developer

## Key Learning

Reading real-world code is different from writing small practice programs. I learned how different Python concepts can work together in one project.