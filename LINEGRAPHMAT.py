import matplotlib.pyplot as plt

dates = [
    '18-05-2017 00:0', '18-05-2017 00:0', '18-05-2017 00:0', '18-05-2017 01:0', '18-05-2017 01:0',
    '18-05-2017 02:0', '18-05-2017 02:0', '18-05-2017 02:0', '18-05-2017 03:0', '18-05-2017 03:0',
    '18-05-2017 03:0'
]

weather_types = [
    'Rain', 'Mist', 'Drizzle', 'Rain', 'Mist',
    'Rain', 'Mist', 'Drizzle', 'Rain', 'Mist','Drizzle'
]

weather_mapping = {'Rain': 3, 'Mist': 2, 'Drizzle': 1}
weather_values = [weather_mapping[w] for w in weather_types]

plt.figure(figsize=(10, 5))
plt.plot(dates, weather_values, marker='o', linestyle='-', color='blue')

plt.xticks(rotation=45)
plt.yticks([1, 2, 3], ['Drizzle', 'Mist', 'Rain'])

plt.title('Weather Type Over Time')
plt.xlabel('Date and Time')
plt.ylabel('Weather Type')
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
