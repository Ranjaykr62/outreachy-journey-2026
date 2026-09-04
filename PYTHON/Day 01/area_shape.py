# Program to calculate area of a rectangle

# Ask for user input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area
area = length * width

# Print result
print("\n--- Rectangle Area ---")
print("Length:", length)
print("Width:", width)
print("Area:", area)


import math

# Input three sides
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Semi-perimeter
s = (a + b + c) / 2

# Area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("\n--- Triangle Area ---")
print("Sides:", a, b, c)
print("Area:", area)
