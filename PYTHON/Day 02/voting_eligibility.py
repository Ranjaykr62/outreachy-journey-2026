# Program to check voting eligibility (Age >= 18 and Indian)

age = int(input("Enter age: "))
citizenship = input("Enter your citizenship: ").lower()

if age >= 18 and citizenship == "indian":
    print("Eligible to vote in India.")
elif age < 18 and citizenship == "indian":
    print("Not eligible: Age must be at least 18.")
else:
    print("Not eligible: Must be an Indian citizen.")
