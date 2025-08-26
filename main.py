from OOP.calculator import Calculator
from OOP.managers import Manager
from OOP.developers import Developer
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


emp1.showDetails()
print()
print("_____******_____****________")
print()
emp2.showDetails()

calc = Calculator()
print(calc.add(1,4,90))