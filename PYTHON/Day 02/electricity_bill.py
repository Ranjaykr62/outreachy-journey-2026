# Program to calculate electricity bill

units = int(input("Enter units consumed: "))

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
elif units <= 500:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
else:
    bill = (100 * 5) + (100 * 7) + (300 * 10) + (units - 500) * 12

print("\n--- Electricity Bill ---")
print("Units Consumed:", units)
print("Total Bill Amount: ₹", bill)
