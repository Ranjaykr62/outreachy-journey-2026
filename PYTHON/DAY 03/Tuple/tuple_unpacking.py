# Create a tuple of 5 numbers
numbers = (10, 20, 30, 40, 50)

# Unpack into separate variables
a, b, c, d, e = numbers

print("First:", a)
print("Second:", b)
print("Third:", c)
print("Fourth:", d)
print("Fifth:", e)


numbers = (10, 20, 30, 40, 50)

#  Using the * operator

# Unpack first, last, and the rest
first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)
