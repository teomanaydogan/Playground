import json
import glob, os
from pprint import pprint

# User inputs
first_name = input("First Name: ")
last_name = input("Last Name: ")
user_name = input("Username: ")
emoji = input("Emoji: ")

# Opens '.json' file and assigns it to 'data'
with open('userdata.json') as f:
    data = json.load(f)

# Appends user inputs to '.json' file
data['users'].append({
    'first_name' : first_name,
    'last_name' : last_name,
    'username' : user_name,
    'emoji' : emoji
})

# Writes user input to '.json'
with open('userdata.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

# Prints data strored in '.json' file
pprint(data)
