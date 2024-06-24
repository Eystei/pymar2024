import json
from typing import Any, Union, List

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


class JsonHandling:

    @staticmethod
    def find_value_by_key(
            data: Union[dict, list],
            key: str,
            find_all: bool = False
    ) -> Union[Any, List[Any], None]:
        """Recursively searches for a value by the given key in a dictionary
        or list with arbitrary nesting. Returns either the first match or all matches
        depending on the `find_all` flag.
        """
        results = []

        def recursive_search(data: Union[dict, list]):
            if isinstance(data, dict):
                for k, v in data.items():
                    if k == key:
                        if find_all:
                            results.append(v)
                        else:
                            return v
                    if isinstance(v, (dict, list)):
                        result = recursive_search(v)
                        if result is not None and not find_all:
                            return result
            elif isinstance(data, list):
                for item in data:
                    result = recursive_search(item)
                    if result is not None and not find_all:
                        return result
            return None

        result = recursive_search(data)
        return results if find_all else result

    @staticmethod
    def deep_value_search(data, target_value, find_all=False):
        """
        Recursively searches for the target value in a dictionary or list
        with arbitrary nesting.

        Args:
            data (Union[dict, list]): The dictionary or list to search within.
            target_value (Any): The value to search for.
            find_all (bool, optional): If True, returns all matching objects.
            If False, returns the first match. Defaults to False.

        Returns:
            Union[dict, list, None]: A list of matching objects if `find_all` is True and matches are found,
                                     a single matching object if `find_all` is False and a match is found,
                                     or None if no matches are found.
        """

        results = []

        def recursive_search(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if value == target_value:
                        results.append(data)
                        if not find_all:
                            return True
                    elif isinstance(value, (dict, list)):
                        if recursive_search(value) and not find_all:
                            return True
            elif isinstance(data, list):
                for item in data:
                    if recursive_search(item) and not find_all:
                        return True

        recursive_search(data)
        return results if results else None
