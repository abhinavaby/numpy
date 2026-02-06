import numpy as np
arr=np.array([1, 2, 3, 4, 5])
print(arr + 5)  # Addition
print()
print(arr - 2)  # Subtraction
print()
print(arr * 3)  # Multiplication
print()
print(arr / 2)  # Division
print()
print(arr ** 2) # Exponentiation
print()
print(arr % 2)  # Modulus   
print()
print()

#aggregate functions
print("Sum of the array:", np.sum(arr))
print("Mean of the array:", np.mean(arr))
print("Standard deviation of the array:", np.std(arr))
print("Minimum value in the array:", np.min(arr))
print("Maximum value in the array:", np.max(arr))
print("Median of the array:", np.median(arr))
print("Variance of the array:", np.var(arr))