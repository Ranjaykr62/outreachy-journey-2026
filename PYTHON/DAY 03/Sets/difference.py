# Create two sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# Difference using difference() method
diff_set = set1.difference(set2)
print("Difference (set1 - set2):", diff_set)

# Difference using - operator
diff_set2 = set2 - set1
print("Difference (set2 - set1):", diff_set2)
