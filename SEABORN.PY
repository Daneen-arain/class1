import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
# Data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 11, 13]

plt.plot(x, y, color='blue', linestyle='-', marker='s', markersize=10)

plt.title('Sales Over Time')
plt.xlabel('Time (months)')
plt.ylabel('Sales')

plt.grid(True)

plt.show()