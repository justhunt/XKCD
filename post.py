#!/usr/bin/env python3
import requests, json
from requests.auth import HTTPBasicAuth
ELASTIC_URL = "https://<URL Endpoint>/xkcd/_bulk"
def elastic():
		r = requests.post(ELASTIC_URL, auth=HTTPBasicAuth('elastic', 'password'), headers = {'content-type': 'application/x-ndjson'}, data = open('6test.json', 'rb'))
		print("Done!")
elastic()
