import json
import sys

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]


def assign_val(data):
    if 'id' in data:
        data_id = data['id']
        if data_id in values_dict:
            data['value'] = values_dict[data_id]

    if 'values' in data:
        for subdata in data['values']:
            assign_val(subdata)


with open(values_file, 'r') as file:
    values = json.load(file)

values_dict = {item['id']: item['value'] for item in values['values']}

with open(tests_file, 'r') as file:
    tests = json.load(file)

for test in tests['tests']:
    assign_val(test)

with open(report_file, 'w') as file:
    json.dump(tests, file)
