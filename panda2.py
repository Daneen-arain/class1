import pandas as pd

data = {
    'Name': ['Avi', 'Mira', 'Zara'],
    'Class': [6, 6, 6],
    'Marks': [85, 92, 78],
    'Fav_Subjects': [['Maths', 'Science'], ['English', 'History'], ['CS', 'Art']]
}

students = pd.DataFrame(data)
print(students)

topper = students['Marks'].describe()
print("Top mark is:", topper)
