# Shopping cart as a list of (item, price)
cart = [
    ("Apple", 50),
    ("Banana", 20),
    ("Milk", 40),
    ("Bread", 30)
]

# Calculate total price
total = 0
for item, price in cart:
    total += price

# Print items and total
print("Shopping Cart:")
for item, price in cart:
    print(item, ":", price)

print("Total Price =", total)
