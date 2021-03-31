#!/usr/bin/env python3

import requests
import os
from pathlib import Path

folder = Path(r'/home/archit/Desktop/fetlife/fetlife.com/js/').rglob('*.txt')

files = [x for x in folder]

working_urls = []
manual_urls = []

for name in files:
	f = open(name, 'r')
	content = f.readlines()
	print(name)	
	#print(content)	
	for url in content:
		try:	
			res = requests.get(url.split()[0])			
			if res.status_code < 400:
			#	print(url, "yes")
				working_urls.append(url)
			#else:
			#	print(url, "no")
		except (requests.ConnectionError, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.InvalidURL) :
			# print("could not get")
			manual_urls.append(url)
	f.close()

output_file = open("valid_urls_checked.txt", "w")
output_file.writelines(working_urls)
output_file.close()

output_file = open("manual_verify_urls.txt", "w")
output_file.writelines(manual_urls)
output_file.close()
