
import json
from pprint import pprint

countries = [
    {"name": "Russia"},
    {"name": "USA"},
]

with open ('example_save.json', 'w') as example_file:
    json.dump(countries, example_file)
