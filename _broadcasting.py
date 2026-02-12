import numpy as np
arr=np.array([10, 20, 30, 40, 50])
discount
# Broadcast the disco to each element in the 
finalprice=arr-(arr*discount/100)
print("Original prices:", arr)
print("Final prices after applying discount:", finalprice)  
print()
arr2=np.array([1,2,3,45,5])
result=arr*2
print("Original array:", arr)
print("Result after broadcasting multiplication:", result)
print()
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
vector=np.array([1,2,3])
result2d=arr2d+vector
print("Original 2D array:")
print(arr2d)
print("Vector to be added:")
print(vector)
print("Result after broadcasting addition:")
print(result2d) 
