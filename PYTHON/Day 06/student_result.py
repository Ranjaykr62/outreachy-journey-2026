class Student:
    def __init__(self, name, roll_number, m1, m2, m3):
        self.name = name
        self.roll_number = roll_number
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total_marks(self):
        return self.m1 + self.m2 + self.m3

    def average_marks(self):
        return self.total_marks() / 3

    def result(self):
        if self.average_marks() >= 40:
            return "Pass"
        else:
            return "Fail"

s = Student("Ranjay", 101, 85, 90, 80)
print("Name:", s.name)
print("Roll Number:", s.roll_number)
print("Total:", s.total_marks())
print("Average:", s.average_marks())
print("Result:", s.result())
