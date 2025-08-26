
from OOP.employees import Employee

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showDetails(self):
        print(super().showDetails())
        print(f"Programming Language: {self.language}")

    def calculate_bonus(self):
        print(self.salary * 0.05 )