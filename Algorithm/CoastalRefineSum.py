

def coastal_sum(list):
    if len(list) == 0:
        return "Empty Dataset"
    total = sum(list)
    if total > 10000:
        print(f"Total delivered: {total} liters ALERT: Capacity Exceeded!")
    return "It is within the Capacity"


print(coastal_sum([1200, 1800, 1500, 2000, 1750, 1400, 1650]))