import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English', 'History']
marks = [85, 90, 75, 80]

plt.plot(subjects,marks,marker='o',color='black')
plt.title('marksin different subjects')
plt.xlabel('subjects')
plt.ylabel('marks')
plt.grid(True)
plt.show()


