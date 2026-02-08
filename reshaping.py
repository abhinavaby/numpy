import numpy as np
arr = np.array([[1, 2, 3,4,5,6]])
reshaped_arr = arr.reshape(2, 3)  # Reshaping to 2 rows and 3 columns does not returs the copy of the array but a view of the original array. It means that any changes made to the reshaped array will affect the original array and vice versa.
print(reshaped_arr)
print()
#flattening the array
array=np.array([[1, 2, 3], [4, 5, 6]])
flattened_array = array.flatten()  # Flattening the array to 1D returns a copy of the array collapsed into one dimension.
print(flattened_array)
print(array)  # Original array remains unchanged
print()
#raveling the array
array2=np.array([[1, 2, 3], [4, 5, 6]])
raveled_array = array2.ravel()  # Raveling the array to 1D returns a view of the original array. It means that any changes made to the raveled array will affect the original array and vice versa.
print(raveled_array)
print(array2)  # Original array remains unchanged