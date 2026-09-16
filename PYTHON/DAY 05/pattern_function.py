# Challenge 5 — Reusable Pattern Generator

def star_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

# Example usage
rows = int(input("Enter rows: "))
star_triangle(rows)

