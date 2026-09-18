class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 85:
            return "A"
        elif self.marks >= 70:
            return "B"
        else:
            return "C"

s = Student("Ranjay", 85)
print("Grade:", s.calculate_grade())
