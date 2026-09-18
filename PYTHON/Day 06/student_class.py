class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Ranjay", 20)
student2 = Student("Amit", 21)

print("Name:", student1.name, "Age:", student1.age)
print("Name:", student2.name, "Age:", student2.age)
