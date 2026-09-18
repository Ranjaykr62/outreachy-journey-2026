class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

emp1 = Employee("Ranjay", 101, 50000)
print(emp1.name, emp1.employee_id, emp1.salary)
