import matplotlib.pyplot as plt
import numpy as np

# Sample Data
students = ['Ali', 'Sara', 'Ahmed', 'Zoya', 'John']
marks = [85, 90, 75, 88, 92]
grades = ['A', 'A+', 'B', 'A', 'A+']

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(students, marks, color='skyblue')
plt.title('Marks of Students')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(marks, labels=students, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Marks Distribution')
plt.tight_layout()
plt.show()

# Line Plot
plt.figure(figsize=(8, 5))
plt.plot(students, marks, marker='o', color='green')
plt.title('Student Performance Line Plot')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.grid(True)
plt.tight_layout()
plt.show()
