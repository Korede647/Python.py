
from OOP.employees import Employee

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def showDetails(self):
        print(super().showDetails())
        print(f"Department: {self.department}")
    
    def calculate_bonus(self):
        return self.salary * 0.10