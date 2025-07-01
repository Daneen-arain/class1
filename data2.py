import numpy as np

# 1. Create an array of student marks
marks = np.array([85, 90, 78, 92, 88])

# 2. Find the average of the marks
average = np.mean(marks)

# 3. Find the maximum and minimum marks
max_mark = np.max(marks)
min_mark = np.min(marks)

# 4. Add bonus marks to each student
bonus = marks + 5

# 5. Filter marks greater than 90
above_90 = marks[marks > 90]

# Print results
print("Original Marks:", marks)
print("Average Marks:", average)
print("Maximum Mark:", max_mark)
print("Minimum Mark:", min_mark)
print("Marks after Bonus:", bonus)
print("Marks above 90:", above_90)
