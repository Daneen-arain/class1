import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 11, 13]

plt.plot(x, y, color='blue', linestyle='--', marker='s')
plt.title('Sales Over Time')
plt.xlabel('Time (months)')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
  