import glob, os
import json
from pprint import pprint

with open('userdata.json') as f:
    data = json.load(f)

pprint(data)
