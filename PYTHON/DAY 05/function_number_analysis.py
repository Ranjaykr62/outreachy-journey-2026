# Challenge 3 — Number Analysis

def count_digits(num):
    return len(str(abs(num)))

def digit_sum(num):
    return sum(int(d) for d in str(abs(num)))

def reverse_number(num):
    return int(str(abs(num))[::-1])

def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Example usage
n = 121
print("Digits:", count_digits(n))
print("Digit Sum:", digit_sum(n))
print("Reverse:", reverse_number(n))
print("Palindrome:", is_palindrome(n))
