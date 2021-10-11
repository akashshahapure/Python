import numpy as np

input_list = [1, 5, 9, 12, 15, 7, 12, 9]
m = 12
n = 6

array_1 = np.array(input_list)
final_array = array_1[(array_1 > m) & (array_1 < n)]

print(final_array)
