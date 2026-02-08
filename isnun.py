import numpy as np
arr=np.array([1, 2, np.nan, 4, 5])
print(np.isnan(arr))
#WE CANNOT COMPARE NAN WITH ANY VALUE, INCLUDING ITSELF
print(arr == np.nan)  # This will return an array of False
print(arr != np.nan)  # This will return an array of True
arr2=np.array([1, np.nan, 3, np.nan, 5])
clear_arr=np.nan_to_num(arr2, nan=0)
print("Original array:", arr2)
print("Array with NaN replaced by 0:", clear_arr)
print() 
arr3=np.array([1, 2, np.inf, -np.inf, 5])
print(np.isinf(arr3))
print()
cleaned_arr=np.nan_to_num(arr3, posinf=9999, neginf=-9999)
print("Original array:", arr3)
print("Array with Inf replaced by 9999 and -Inf replaced by -9999:", cleaned_arr)

