import json
from pprint import pprint

filepath = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/02_Code/recipes/linkscraping_preferences.json"

with open(filepath) as data_file:    
    data = json.load(data_file)

# pprint(data)

print json.dumps(data, indent=4, sort_keys=True)

