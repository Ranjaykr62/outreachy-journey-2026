# Program to calculate salary bonus

salary = float(input("Enter your salary: "))

if salary < 20000:
    bonus = 0.20 * salary   # 20% bonus
elif salary <= 50000:
    bonus = 0.15 * salary   # 15% bonus
else:
    bonus = 0.10 * salary   # 10% bonus

print("\n--- Salary Bonus Details ---")
print("Salary:", salary)
print("Bonus:", bonus)
print("Total (Salary + Bonus):", salary + bonus)
