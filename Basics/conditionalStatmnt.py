def userAge(age):
    if age < 18:
        return 'You are not qualified to apply🤧.'
    
    return "Congrats! You're qualified👌. "
    
age = userAge(10)

# print(age)

balance = 0

def ATM(input):
    if input == 1:
        amount = 2300
        deposit(amount)
        return
    if input == 2:
        amount = 1200
        withdrawal(amount)
        return
    if input == 3:
        inquire()
        return
    return "No input"



def deposit(amount):
    return balance + amount


def withdrawal(amount):
    if amount < balance:
        "Insufficient funds"
    bal = balance-amount
    return balance

def inquire():
    return f"Your balance is {balance}.0"

task = ATM(3)
print(task)