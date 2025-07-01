import pandas as pd

# Sample data
data = {
    'Name': ['noah', 'eshaal', 'annalee', 'Daneen', 'Elias'],
    'Maths': [85, 90, 78, 92, 88],
    'Science': [89, 75, 84, 95, 91]
}

# Create a DataFrame
df = pd.DataFrame(data)

# 1. Add a new column for average marks
df['Average'] = (df['Maths'] + df['Science']) / 2

# 2. Filter students with average >= 85
high_achievers = df[df['Average'] >= 85]

# 3. Sort the DataFrame by average marks in descending order
sorted_df = high_achievers.sort_values(by='Average', ascending=False)

# Print the final DataFrame
print("High Achievers (Average >= 85):")
print(sorted_df)
