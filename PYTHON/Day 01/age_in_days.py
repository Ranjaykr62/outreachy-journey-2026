# Program to calculate how long you have lived

# Ask for user input
age_years = int(input("Enter your age in years: "))

# Convert age into months, weeks, and days
months = age_years * 12
weeks = age_years * 52   # Approximation (ignores leap years)
days = age_years * 365   # Approximation (ignores leap years)

# Print results
print("\n--- Life Duration Summary ---")
print("You have lived for:")
print("Years :", age_years)
print("Months:", months)
print("Weeks :", weeks)
print("Days  :", days)
