import json

data = {'name': 'Nastya', 'surname': 'Petrishche', 'age': '17'}

with open('file_03.json', 'w') as file:
    json.dump(data, file)

