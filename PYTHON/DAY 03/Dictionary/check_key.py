student = {
    "Name": "Ranjay Kumar",
    "Age": 21,
    "College": "IIT Patna",
    "Python Marks": 85
}

# Check if key exists
if "Age" in student:
    print("Key 'Age' exists")
else:
    print("Key 'Age' does not exist")


if student.get("Physics Marks") is not None:
    print("Key 'Physics Marks' exists")
else:
    print("Key 'Physics Marks' does not exist")
