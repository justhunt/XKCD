#!/usr/bin/env python3
import json, requests, datetime, sys
from datetime import datetime, date
from requests.auth import HTTPBasicAuth

URL = "https://<URL Endpoint>/xkcd/_search?pretty"
results = {}

###Gets the last comic number from our database. This will be used for the base value of range when we need to update our database###
query = json.dumps({
	"size": 0,
	"aggs": {
		"max_id": {
			"max": {
				"field": "num" } } } }
)
response = requests.get(URL, data=query, auth=HTTPBasicAuth('elastic', 'password'), headers={'content-type': 'application/json'})
results = json.loads(response.text)
for k in results:
	if k == 'aggregations':
		for y in results[k]:
			if y == 'max_id':
				for u in results[k][y]:
					u = results[k][y]['value']		#Gets the last comic number in our database
					if u is None:				#If there are no comics in the database then set the comic number to 0
						u = 1 
					elif u is not None:			#If there IS a comic number, turn that number into an integer
						u = int(results[k][y]['value'])
#						print(u)			#What number is the last comic in our database

###Finds the number of the most recent comic posted. This will be used for the max value of our range for when we need to update our database###
currentDay = datetime.now()
ordinal = currentDay.toordinal()
stop_int = int(ordinal)
stop = (stop_int-735035)

###Gets all of the xkcd comics json data and stores it to the 6test.json file###
def main():
	f = open("6test.json", "w")
	for n in range(u, stop):
		key = ('{ "index" : { "_index" : "xkcd", "_id" : %d}}' % n)
		value_json_data = requests.get("http://xkcd.com/%d/info.0.json" % n)
		if value_json_data.status_code == 200:
			value_json_dict = value_json_data.json()
			value = json.dumps(value_json_dict)
			f.write(key + "\n" + value + "\n")
			print(key)
		elif value_json_data != 200:
			print(value_json_data)
			print(n)
			if n == "403":
				n+1	
			
main()
