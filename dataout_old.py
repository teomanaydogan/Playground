import json
import glob, os
import emoji
from pprint import pprint

first_name = input("First Name: ")
last_name = input("Last Name: ")
user_name = input("Username: ")
emoji = input("Emoji: ")

userdata = {}

userdata['users'] = []

userdata['users'].append({
    'first_name':first_name,
    'last_name':last_name,
    'username':user_name,
    'emoji':emoji
})


with open('userdata_new.json', 'w') as outfile:
    json.dump(userdata, outfile, indent=4)
