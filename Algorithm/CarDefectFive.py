

def car_defect_5(list):
    if len(list) == 0:
       return "Empty Dataset"
    exceedLimit = []
    for num in list:
        if num > 5:
            exceedLimit.append(num)
    return exceedLimit


print(car_defect_5([2, 8, 1, 0, 6, 7, 3, 9, 5]))