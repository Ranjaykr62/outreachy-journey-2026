rows = 5

for i in range(1, rows + 1):
    # spaces
    j = 1
    while j <= rows - i:
        print(" ", end="")
        j += 1
    # stars
    k = 1
    while k <= i:
        print("* ", end="")
        k += 1
    print()
