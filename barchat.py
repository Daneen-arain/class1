import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English', 'History']
marks = [85, 90, 75, 80]

plt.bar(subjects, marks, color='skyblue')
plt.title('Marks in Different Subjects')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.grid(True)
plt.show()
