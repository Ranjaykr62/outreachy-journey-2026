class NumberAnalyzer:
    def __init__(self, number):
        self.number = number

    def is_even(self):
        return self.number % 2 == 0

    def is_prime(self):
        if self.number < 2:
            return False
        for i in range(2, int(self.number**0.5) + 1):
            if self.number % i == 0:
                return False
        return True

    def reverse(self):
        return int(str(self.number)[::-1])

    def is_palindrome(self):
        return str(self.number) == str(self.number)[::-1]

n = NumberAnalyzer(121)
print("Even:", n.is_even())
print("Prime:", n.is_prime())
print("Reverse:", n.reverse())
print("Palindrome:", n.is_palindrome())
