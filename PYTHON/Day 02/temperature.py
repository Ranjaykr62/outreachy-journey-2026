# Program to check temperature category

temp = float(input("Enter temperature in °C: "))

if temp < 20:
    print("Temperature is Cold.")
elif 20 <= temp <= 30:
    print("Temperature is Normal.")
else:
    print("Temperature is Hot.")
