#!/usr/bin/env python3
import json, string, requests
from requests.auth import HTTPBasicAuth
URL = "https://c85eff0a49b345feb08db5d00c7b79e9.us-central1.gcp.cloud.es.io:9243/xkcd/_search?q="
xkcd = {}

###Asks the user what they would like to search for###
word = input("Is there and XKCD for that? Let's find out! Please tell me what you would like to find: ")

###Takes the input from the user and searches our database for the word###
search = requests.get(url = URL + word, auth = HTTPBasicAuth('elastic', 'LyIlTmQtozDEJubpkpqwwbNU'))

###finds a good search result and puts all of the data into a dictionary so we can manipulate what info we want###
xkcd = json.loads(search.text)

###Manipulation of data underway###
for k in xkcd:
	if k == "hits":		
		for y in xkcd[k]:
			if y == "hits":		
				for j in  xkcd[k][y][0]:
					if j == "_source":	
						print("Title: " + str(xkcd[k][y][0][j]["title"]) + "\nID: " + str(xkcd[k][y][0]["_id"]) + "\nImage Link: " + str(xkcd[k][y][0][j]["img"]) + "\nDate Created: " + str(xkcd[k][y][0][j]["month"] + "-" + str(xkcd[k][y][0][j]["day"]) + "-" + str(xkcd[k][y][0][j]["year"])) + "\nTranscript: " + str(xkcd[k][y][0][j]["transcript"]))



#####Notes for hunter#####
#k = "hits"
#y = "hits"
#print("score:" + str(xkcd[k][y][0]["_score"]) + "\nid: " + str(xkcd[k][y][0]["_id"]))

#print("score:" + str(xkcd["hits"]["hits"][0]["_score"]) + "\nid: " + str(xkcd["hits"]["hits"][0]["_id"]))

##TO PRINT COMPLETE JSON##
#print(json.dumps(xkcd, indent=4))

##TO PRINT THE FIRST HITS##
#for k in xkcd:
#        if k == "hits":
#		print(json.dumps(xkcd[k], indent=4))
