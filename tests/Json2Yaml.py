# Python script to Read file from JSON and convert to YAML
# Author - yucheng.hu@insight.com

import datetime
import json

import ruamel.yaml as yaml
from dateutil.relativedelta import relativedelta

json_filename = 'resources/black_rock_test.json'
yaml_filename = 'resources/black_rock_test.yaml'

ELIGIBLE_FOR_RETIREMENT = 'eligible_for_retirement'


# Get Difference Years
def get_age(data_input):
    date_user = datetime.datetime.strptime(data_input, '%m/%d/%Y')
    date_current = datetime.datetime.now()

    time_difference = relativedelta(date_current, date_user)
    return time_difference.years


# Read and process JSON
with open(json_filename) as json_file:
    data = json.load(json_file)
    data_bod = data['date_of_birth']

    if get_age(data_bod) >= 65:
        data[ELIGIBLE_FOR_RETIREMENT] = True
    else:
        data[ELIGIBLE_FOR_RETIREMENT] = False

# Write to YAML
with open(yaml_filename, 'w') as yaml_file:
    yaml.dump(data, yaml_file, allow_unicode=True, default_flow_style=False)
