from message import getUser_name
from message import getUser_name as username
from message import user
import datetime
import platform
import math
import json

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

print(dt.timetuple)

# print(dt.strftime("%A"))
# print(dt.strftime("%dth"))
# print(dt.year)

# print(math.sin(30))
# print(pow(3,3))
numbers = max(45, 3, 43, 89, 24, 12)
# print(numbers)

product = '{"name": "Hero", "age": 23, "city": "rivers" }'

print(json.loads(product))
pdc = json.loads(product)
print(type(pdc))

# object as string
us = json.dumps(user)
print(us.upper())