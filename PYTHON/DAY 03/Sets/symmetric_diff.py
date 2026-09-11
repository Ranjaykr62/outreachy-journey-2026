set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# Symmetric difference
print(set1 ^ set2)




# Create two sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# Symmetric difference using symmetric_difference() method
sym_diff = set1.symmetric_difference(set2)
print("Symmetric difference:", sym_diff)

# Symmetric difference using ^ operator
sym_diff2 = set1 ^ set2
print("Symmetric difference (using ^):", sym_diff2)
