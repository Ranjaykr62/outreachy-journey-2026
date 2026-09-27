# Day 12 - Code Reading Practice


def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def calculate_average(numbers):
    total = calculate_total(numbers)

    average = total / len(numbers)

    return average


marks = [80, 90, 70, 60]

total_marks = calculate_total(marks)
average_marks = calculate_average(marks)

print("Total:", total_marks)
print("Average:", average_marks)



# Q1. What is the purpose of calculate_total()?
# Answer: calculate_total() adds all the numbers in a list and returns their total.


# Q2. What does the variable total store?
# Answer: total stores the sum of all the numbers processed by the loop.


# Q3. What does the for loop do?
# Answer: The for loop goes through each number in the list and adds it to total.


# Q4. What does calculate_total(numbers) return?
# Answer: It returns the total sum of all the numbers in the list.


# Q5. What does len(numbers) do?
# Answer: len(numbers) returns the number of items in the list.


# Q6. What is the final value of total_marks?
# Answer: The final value of total_marks is 300.


# Q7. What is the final value of average_marks?
# Answer: The final value of average_marks is 75.0.


# Q8. Which function is called first?
# Answer: calculate_total() is called first.


# Q9. Which function calls another function?
# Answer: calculate_average() calls calculate_total().


# Q10. Explain the complete program in 3-5 sentences.
# Answer:
# The program calculates the total and average of a list of marks.
# The calculate_total() function adds all the marks together.
# The calculate_average() function uses the total to calculate the average.
# Finally, the program prints the total marks and average marks.

. 