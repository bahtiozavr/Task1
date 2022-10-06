import json

with open('info.json', 'r') as info_file:
    info_data = json.load(info_file)
    print(json.dumps(info_data, indent=4, sort_keys=True))
