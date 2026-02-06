import numpy as np
#list to array
l=[1,2,3,4,5]
array_from_list=np.array(l)
print("Array from list:")
print(array_from_list)
print()




#with difault values. 




# syntax: np.zeros(shape) (3) fir dim , (3,3) for 2 dim
zero_array=np.zeros(3)
print("Array with default zero values:")
print(zero_array)
print()
#ones array ones(shape)
ones_array=np.ones((2,3))
print("Array with default one values:")
print(ones_array)
print()


#full array full(shape,fill_value)
full_array=np.full((2,2),7)
print("Array with default fill value:")
print(full_array)
print()


#sequence of numbers arange(start, stop, step)
sequence_array=np.arange(0,10,2)
print("Array with sequence of numbers:")
print(sequence_array)
print()


#identity matrix eye(n)
identity_matrix=np.eye(4)
print("Identity matrix:")
print(identity_matrix)
print()
