car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "automatic_transmission": True,
    "colors": [ "red", "white", "blue"]
}

# print(car)
# print(type(car))

# print(len(car))

# get one item in the dictionary
# print(car.get("model"))

ky = car.keys()
# print(ky)

car["tinted"] = ["Factory", "Grade 0", "Grade 1"]

# print(car)

values = car.values()
# print(values)

# print all the items
# print(car.items())

if "year" in car:
    car["year"] = 2025

# print(car)

# delete from dict
# car.pop("model")

# del car["model"]

# del car
# print(car)

# for x in car:
#     if x.startswith("b"):
#        result = x.upper()
#        print(result)

# for value in car.values():
#     print(value)

# for ky in car.keys():
#     print(ky)

# mycopy = car.copy()
# print(mycopy)

# my_copy = dict(car)
# print(my_copy)

user = { "name": "Maro", "gender": "Female", "skills": ["TIKTOK", "JavaScript", "HTML"]}

user1 = { "name": "Korede", "gender": "Female", "skills": ["Python", "JavaScript", "HTML"]}

user2 = { "name": "Alexander", "gender": "Male", "skills": ["Python", "TypeScript", "HTML"]}

users = { "first": user, "second": user1, "third": user2}

# print(users)

print(users["first"]["skills"][-1])  # Accessing the last skill of the first user



