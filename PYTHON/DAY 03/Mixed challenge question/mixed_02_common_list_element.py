# Two lists with some common numbers
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)

# Find common elements (intersection)
common = set1 & set2

print(common)
