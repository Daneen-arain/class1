student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english', 'maths', 'science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english', 'maths', 'science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english', 'maths', 'science']
    },
    'id4': {
        'name': ['Mehtej'],
        'class': ['V'],
        'subject_integration': ['english', 'maths', 'science']
    }
}

print('no. 1', student_data['id1'])
print('no. 2', student_data['id2'])
print('no. 3', student_data['id3'])
print('no. 4', student_data['id4'])

x = student_data.values()
print(x)
