#!/usr/bin/env python3

import requests
import os
from pathlib import Path

folder = Path(r'/home/archit/Desktop/recon/urls/').rglob('*.txt')

files = [x for x in folder]

working_urls = []

for name in files:
	f = open(name, 'r')
	content = f.readlines()
	print(name)	
	#print(content)	
	for url in content:
		try:
			res = requests.get(url)
			if res.status_code < 400:
				# print(url, "yes")
				working_urls.append(url)
			#else:
			#	print(url, "no")
		except (requests.ConnectionError, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.InvalidURL):
			print("could not get")
	
	f.close()


output_file = open("valid_urls_checked.txt", "w")
output_file.writelines(working_urls)
output_file.close()


