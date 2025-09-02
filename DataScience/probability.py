import numpy as np

purchases = np.array([10, 20, 30, 200, 300])

mean_value = purchases.mean()

# print(mean_value)

salary = np.array([500, 600, 700, 800, 1000, 10000, 50000 ])

# print(salary.mean())

data = np.array([45, 50, 52, 55, 60, 65,150, 200])

average = data.mean()
middle = np.median(data)
print(middle, average)
print(f"Mean: {average}\nMedian: {middle}")