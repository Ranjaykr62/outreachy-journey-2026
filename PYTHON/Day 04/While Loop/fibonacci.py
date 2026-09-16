# Generate Fibonacci series up to n terms using while loop

n = int(input("Enter number of terms: "))  # user input
a, b = 0, 1   # first two terms
count = 0

print("Fibonacci Series:")

while count < n:
    print(a, end=" ")   # print current term
    a, b = b, a + b     # update values
    count += 1          # increment counter
