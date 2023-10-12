import json
import yaml

with open('sample.json', 'r') as json_file:
    ourjson = json.load(json_file)

print(ourjson)

print("The ip is {}".format(ourjson['ip']))
print("The memory is {}".format(ourjson['memory']))

print('\n\n')
print(yaml.dump(ourjson))