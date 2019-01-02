import glob, os
import json
from pprint import pprint

user = input('0, 1, 2, 3, 4 : ')

service = True

with open('userdata.json') as f:
    data = json.load(f)

userdata = data['users'][int(user)]
username = userdata['username']


while service == True:
    cmd_prmt = input(username+": ")
    cmd_prmt = cmd_prmt.strip()

    if cmd_prmt == 'name':
        print(userdata['first_name'], userdata['last_name'])

    if cmd_prmt == 'emoji':
        print(userdata['emoji'])

    if cmd_prmt == 'q':
        service = False
