# Store multiple student records in a file
with open("student_records.txt", "a") as f:
    while True:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        f.write(f"Name: {name}, Age: {age}, Course: {course}\n")

        choice = input("Add another student? (y/n): ")
        if choice.lower() != "y":
            break

print("Student records saved!")
