import json

with open('file_03.json', 'r') as file:
    data = json.load(file)
    print(data)