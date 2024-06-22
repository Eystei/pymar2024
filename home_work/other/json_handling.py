import json
from typing import Any, Union

# METHOD 1: WRITE & READ FILE THROUGH SERIALIZATION & DESERIALIZATION STRING

data_dict = {
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}

json_str = json.dumps(data_dict, indent=2)

with open(file='temp_data/data_file.json', mode='w', encoding='utf-8') as f:
    f.write(json_str)

with open('temp_data/data_file.json', mode='r', encoding='utf-8') as f:
    json_str_from_file = f.read()

data_dict_from_file = json.loads(json_str_from_file)

# METHOD 2: WRITE & READ JSON DIRECTLY IN/FROM FILE

data_dict_1 = {
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}

with open(file='temp_data/data_file_1.json', mode='w', encoding='utf-8') as f:
    json.dump(obj=data_dict_1, fp=f, indent=2)

with open(file='temp_data/data_file_1.json', mode='r', encoding='utf-8') as f:
    dict_from_json_file = json.load(fp=f)


def find_value_by_key(data: Union[dict, list], key: str) -> Any:
    """Recursively searches for a value by the given key in a dictionary
    or list with arbitrary nesting.
    """
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                return v
            elif isinstance(v, (dict, list)):
                result = find_value_by_key(v, key)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for item in data:
            result = find_value_by_key(item, key)
            if result is not None:
                return result
    return None
