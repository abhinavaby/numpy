import numpy as np
array=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2D Array:")
print(array)
print("Shape of the array:", array.shape)
array_size=array.size
print("Size of the array:", array_size)
print("Number of dimensions:", array.nd
print("Data type of the array:", array.dtype)


      \
print()
#changing data type
array_float=array.astype(float)
print("Array with float data type:")
print(array_float)
print("Data type of the new array:", array_float.dtype)
