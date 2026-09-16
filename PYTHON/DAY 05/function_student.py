# Challenge 2 — Student Marks

def total_marks(marks):
    return sum(marks)

def average_marks(marks):
    return sum(marks) / len(marks)

def highest_mark(marks):
    return max(marks)

def lowest_mark(marks):
    return min(marks)

def pass_fail(marks, passing_score=40):
    return ["Pass" if m >= passing_score else "Fail" for m in marks]

# Example usage
marks = [75, 40, 89, 32, 56]
print("Total:", total_marks(marks))
print("Average:", average_marks(marks))
print("Highest:", highest_mark(marks))
print("Lowest:", lowest_mark(marks))
print("Pass/Fail:", pass_fail(marks))
