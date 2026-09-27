## Day 12 - Debugging Challenge


def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    return average


marks = [80, 90, 70]

print("Average:", calculate_average(marks))