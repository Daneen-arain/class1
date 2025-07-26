import pandas as pd
import matplotlib.pyplot as plt

data = {'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        'Temperature': [22, 24, 19, 23, 25]}

df = pd.DataFrame(data)
 
df.plot(x='Day', y='Temperature', kind='line', marker='o')
plt.title('Temperature Over Days')

plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

