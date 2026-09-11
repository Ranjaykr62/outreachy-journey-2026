# Student dictionary
student = {
    "Name": "Ranjay Kumar",
    "Age": 21,
    "College": "IIT Patna",
    "Python Marks": 85
}

# Update existing values
student["Age"] = 22              # Update age
student["Python Marks"] = 95     # Update Python marks

print("Updated Student Dictionary:")
print(student)


student.update({
    "Age": 23,
    "College": "IIT Delhi"
})

print("Updated Student Dictionary:", student)
