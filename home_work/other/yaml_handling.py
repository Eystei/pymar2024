from pprint import pprint
import yaml

from home_work.other.json_handling import JsonHandling

with open('_test.yaml') as f:
    dict_ = yaml.safe_load(f)

a = JsonHandling.find_value_by_key(data=dict_, key='name', find_all=True)

# pprint(dict_)

b = JsonHandling.deep_value_search(data=dict_, target_value='Amina', find_all=True)

pprint(a)
