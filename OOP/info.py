# class Info():
    # greet = "How are you?"

# print(Info)

# info1 = Info()

# print(info1.greet)


class Person():
    def __init__(self, firstName, lastName): #init is automatically created when a method is created in a class
        self.firstName = firstName  #self is like this in java
        self.lastName = lastName

    def __str__(self):
        return f"FullName: {self.firstName} {self.lastName}"
    
    def user_details(self):
        return f"Name: {self.firstName} {self.lastName}"

p1 = Person("Korede", "Zion")
p2 = Person("Peace", "Alexander")
p3 = Person("Michael", "Adebayo")
# p1.lastName = "Prince"
# print(p1.firstName)
# print(p1.lastName)

# print(p1)
# print(p1.user_details())
# print(p3.user_details())