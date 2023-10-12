import json
import yaml

with open('sample.yaml', 'r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

print(ouryaml)

print('\n')
print("The ip is {}".format(ouryaml['ip']))
print("The memory is {}".format(ouryaml['memory']))

print('\n')
print(json.dumps(ouryaml, indent=4))