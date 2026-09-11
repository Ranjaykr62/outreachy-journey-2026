# Create three sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
set3 = {40, 30, 70, 80}

# Intersection using intersection() method
common_elements = set1.intersection(set2, set3)
print("Common elements:", common_elements)

# Intersection using & operator
common_elements2 = set1 & set2 & set3
print("Common elements (using &):", common_elements2)
