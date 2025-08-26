# inheritance

class Employee: 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def showDetails(self):
        return f"Employee Name: {self.name}\nSalary: {self.salary}"
    
    def calculate_bonus(self):
        print(self.salary * 0.05)