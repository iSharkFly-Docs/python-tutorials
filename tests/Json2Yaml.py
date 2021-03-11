# Python script to Read file from JSON and convert to YAML
# Author - HoneyMoose (https://www.ossez.com)

import json
import ruamel.yaml as yaml

json_filename = 'resources/black_rock_test.json'
yaml_filename = 'resources/black_rock_test.yaml'

# Read and process JSON
with open(json_filename) as json_file:
    data = json.load(json_file)
    print(type(data))

    for data_dict in data:
        label_id = data_dict['label_id']
        print(str(label_id))
json_file.close()

# Write to YAML
yaml_file = open(yaml_filename, 'w+')
yaml.dump(data, yaml_file, allow_unicode=True)
yaml_file.close()
