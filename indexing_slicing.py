import numpy as np  
arr=np.array([1,2,3,4,5])
print(arr[1])  # Accessing the second element
print(arr[0:3])  # Slicing the first three elements
print(arr[::2])  # Slicing with a step of 2
print(arr[-1])  # Accessing the last element
print(arr[-3:])  # Slicing the last three elements
print(arr[::-1])  # Reversing the array
print(arr[1:4:2])  # Slicing with a step of 2
print()
#fancy indexing
print(arr[[0, 2, 4]])  # Accessing specific elements using a list of indices
print(arr[[1, 3]])  # Accessing specific elements using a list of indices
print()
#filtering with boolean indexing
print(arr[arr > 2])  # Accessing elements greater than 2
print(arr[arr % 2 == 0])  # Accessing even elements

