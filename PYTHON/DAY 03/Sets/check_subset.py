set1 = {10, 20, 30}
set2 = {10, 20, 30, 40, 50}

# Check subset
print(set1.issubset(set2))   # True



# Create two sets
set1 = {10, 20, 30}
set2 = {10, 20, 30, 40, 50}

# Using issubset()
print("Is set1 a subset of set2?", set1.issubset(set2))

# Using <= operator
print("Is set1 a subset of set2?", set1 <= set2)

# Proper subset check (strictly smaller)
print("Is set1 a proper subset of set2?", set1 < set2)
