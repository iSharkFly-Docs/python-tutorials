# Python script to Read file from JSON and convert to YAML
# Author - HoneyMoose (https://www.ossez.com)

import json

json_filename = 'resources/honeymoose_test.json'

# Read and process JSON
with open(json_filename) as json_file:
    data = json.load(json_file)
    print(type(data))

    for data_dict in data:
        label_id = data_dict['label_id']
        print(str(label_id))

print(json_file.closed)
