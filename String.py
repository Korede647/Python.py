name = "Prince"
# print(name[0])

# sentence = """This is the girl I truly Love
# But she doesn't know I exist religion is standing between us
# I am not sure if she will ever know
# Oh God! Help me
# I am not sure if I will ever tell her
# """

# print(sentence)

school = "University of Lagos"

# for x in school:
#     print(x)

# string length
# print(len(school))

# how to check if part of a string exists
# if "Lagos" in school:
#     print("Lagos is part of the string")
# else :
#     print("Lagos is not part of the string")

# if "Lagos" not in school:
#     print("Lagos is part of the string")
# else :
#     print("Lagos is not part of the string")

# slicing
message = "I Love Michael B Jordan"
# print(message[2:6])  

message= "This is the place"
# print(message[12:])  # prints 'is the place'

# print(message[:4])   # prints 'This'
# print(message[-5:-2])
# 
# print(message.upper())  # converts to uppercase
# print(message.lower())  # converts to lowercase
# print(message.title())  # converts to title case

msg = "    Hello"
# print(len(msg.strip()))
# print(len(msg))

ex = "Uche, Bimbo, Mario"
# print(ex.replace("Bimbo", "Comfort"))

newStr = ex.split(", ")
# print(type(newStr))
# print(newStr)

# Format string
friend = "James"
# print(f"Mr friend's name is {friend}")
# txt = "I love {0} and {1}".format("Python", "Java")
text = f"The handsome guy in the class is {friend}"
# print(text)

price = 45
txt2 = f"The current price of the item is {price: .2f} dollars"
# print(txt2)

qty = 3
unit_price = 400
total_sale = f"Total: {qty * unit_price}"
# print(total_sale)

user_name = "alexander, door"

# print(user_name.capitalize())
# print(user_name.count('a', 5, 7))
# print(user_name.endswith("door"))

account_number = "abdeft"
# print(account_number.isalpha())
# print(account_number.isalnum())

# reverse string
# hello => olleh
def reverseStr(str):
    return str[::-1]

# print(reverseStr("hello"))

# write python to verify if a given string is palidrome or not

def isPalindrome(str):
    newStr= str.lower()
    return newStr[::-1] == newStr

# print(isPalindrome("EbuBe"))

def countVowel(str):
    vowels = "aeiouAEIOU"
    return sum(1 for char in str if char in vowels)

print(countVowel("MIke"))