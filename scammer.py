#!/bin/bash
import requests
import os
import random
import string
import json


chars = string.ascii_letters + string.digits + "!@#$%^&*()"
random.seed = (os.urandom(1024))

url = "CHANGEME"

names = json.loads(open('names.json').read())


for name in names:
	name_extra = ''.join(random.choice(string.digits))
	username = name.lower() + name_extra

	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data = {
		'CHANGEME': username,
		'CHANGEME': password 
		})

	print(f"Sending {username} and password {password}")




