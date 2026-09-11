# Create two sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# Elements in set1 but not in set2
diff1 = set1.difference(set2)
print("Elements in set1 but not in set2:", diff1)

# Elements in set2 but not in set1
diff2 = set2 - set1
print("Elements in set2 but not in set1:", diff2)
