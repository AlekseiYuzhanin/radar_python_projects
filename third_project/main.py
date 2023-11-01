import numpy as np

colum_1 = np.array([0, 1, 3, 1, 0])
colum_2 = np.array([1, 3, 1, 4, 1])
colum_3 = np.array([4, 1, 3, 5, 4])
colum_4 = np.array([4, 8, 4, 8, 5])
colum_5 = np.array([7, 1, 3, 1, 0])

matrix = np.column_stack((colum_1, colum_2, colum_3, colum_4, colum_5))

np.fill_diagonal(matrix, 5)

random_array = np.random.randint(-10, 1, size=matrix.shape)

result = np.dstack((matrix, random_array))

print(result)