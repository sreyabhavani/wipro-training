import numpy as np
import pandas as pd
np.random.seed(42)
data_array=np.random.randint(1,501,size=(10,10))
print("Original Array:\n")
print(data_array)
global_mean=np.mean(data_array)
modified_array=data_array.copy()
modified_array[modified_array>global_mean]=0
print("\nGlobal Mean:", global_mean)
print("\nModified Array:\n")
print(modified_array)

# 2. Sum of each column and standard deviation of each row
column_sum = np.sum(data_array, axis=0)
row_std = np.std(data_array, axis=1)

print("\nColumn Sums:\n", column_sum)
print("\nRow Standard Deviations:\n", row_std)

# 3. Extract center 4x4 sub-matrix and flatten
sub_matrix = data_array[3:7, 3:7]

flat_array = sub_matrix.flatten()

print("\nCenter 4x4 Sub-Matrix:\n")
print(sub_matrix)

print("\nFlattened 1D Array:\n")
print(flat_array)


