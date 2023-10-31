import json

a = input('name')
b = input('surname')
c = input('age')

data = {'name': a, 'surname': b, 'age': c}

with open('file_04.json', 'w') as file:
    json.dump(data, file)
