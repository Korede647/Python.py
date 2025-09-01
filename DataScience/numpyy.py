import numpy as np

arr = np.array((45)) # Create 0D array
# print(type(arr))

arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]]) #3D array
# print(arr2.ndim)
# print(arr2[2,1]) #Access specific element in array

# arr = np.array([1,2,3,4,5], ndim = 6) 

# lst = [10, 20, 30, 40, 50]
# arr = np.array([10, 20, 30, 40, 50])

# fruits = np.array(["mango", "apple", "lemon", "orange"])

#Type cast from array to numpy array (Convert from one type to another) ......???

#try out
# arr5 = np.array([10, 20, 30, 40, 50, 60])
# print(arr5)
# newArr = arr5.astype("i")
# print(newArr)
# print(arr5.dtype)
# print(newArr.dtype)
EdArr = np.array([[1,2,3], [20, 15, 27], [45, 35, 32]])
# print (EdArr.shape) # prints how many row & column the matrix has
# print(EdArr.size)

# print(EdArr[0,0])

# print(np.random.rand(2,2))
# print(np.random.rand(1,10))
# print(np.random.rand(100,10))

sales = np.array([
    [50, 30, 20],
    [60, 35, 22],
    [55, 40, 25],
    [70, 45, 30],
    [65, 42, 28]
])
print("Sales Data: \n", sales)
print("Total per product: ", sales.sum(axis=0))
print("Total sales per day: ", sales.sum(axis=1))
print("Average eggs sold per day: ", sales[::,2].mean())