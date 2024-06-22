from pprint import pprint
import yaml

with open('temp_data/data.yaml') as f:
    temp = yaml.safe_load(f)

pprint(temp)
print(type(temp))

