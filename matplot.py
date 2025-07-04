import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English', 'History']
marks = [85, 90, 75, 80]

plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90)
plt.title('Marks Distribution in Subjects')
plt.axis('equal')
plt.show()
