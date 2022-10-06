import json

with open('info.json', 'r') as info_file:
    info_data = json.load(info_file)
    print(info_data)
