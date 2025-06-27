import numpy as np
students = np.array([
    [1, 14, 160],
    [2, 13, 155],
    [3, 14, 158],
    [4, 15, 160],
    [5, 13, 150],
    [6, 14, 158],
    [7, 15, 162],
    [8, 13, 160],
    [9, 14, 155],
    [10, 15, 160]
])
sorted_indices = np.lexsort((students[:, 1], students[:, 2]))
sorted_students = students[sorted_indices]
print("ID  Age  Height")
print(sorted_students)