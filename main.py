from OOP.calculator import Calculator
from OOP.managers import Manager
from OOP.developers import Developer
from OOP.bank import BankAccount
from OOP.employees import Employee
from message import getUser_name
from message import getUser_name as username
from message import user
import datetime
import platform
# import math
import json
# from math.geometry import areaOfCircle, areaOfRectangle
# from math.algebra import add, multiply


# print(getUser_name("Korede"))
# print(username("Korede"))

# pf = platform.system()
# print(pf)
pf = dir(platform)
# print(pf)

# print(user["age"])
dt = datetime.datetime.now()
# print(type(dt))
# print(dt.year)

# print(dt.timetuple)

# print(dt.strftime("%A"))
# print(dt.strftime("%dth"))
# print(dt.year)

# print(math.sin(30))
# print(pow(3,3))
numbers = max(45, 3, 43, 89, 24, 12)
# print(numbers)

product = '{"name": "Hero", "age": 23, "city": "rivers" }'

# print(json.loads(product))
pdc = json.loads(product)
# print(type(pdc))

# object as string
us = json.dumps(user)
# print(us.upper())

emp1 = Manager("Nathan", 5000, "IT")
emp2 = Developer("Prince", 2300, "TYPESCRIPT")
emp3 = Employee("Korede", 5000)
emp4 = Employee("Alexander", 2300)


# emp1.showDetails()
# print()
# print("_____******_____****________")
# print()
# emp2.showDetails()

# emp3.calculate_bonus()
# print()
# print("_____******_____****________")
# print()
# emp4.calculate_bonus()
# emp2.calculate_bonus()
# print()
# print("_____******_____****________")
# print()
# emp1.calculate_bonus()


# calc = Calculator()
# print(calc.add(1,4,90))

# acc = BankAccount("Inala", 4500)
# acc.deposit(45000)
# print(acc.getBalance())