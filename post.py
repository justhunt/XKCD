#!/usr/bin/env python3
import requests, json
from requests.auth import HTTPBasicAuth
ELASTIC_URL = "https://c85eff0a49b345feb08db5d00c7b79e9.us-central1.gcp.cloud.es.io:9243/xkcd/_bulk"
def elastic():
		r = requests.post(ELASTIC_URL, auth=HTTPBasicAuth('elastic', 'LyIlTmQtozDEJubpkpqwwbNU'), headers = {'content-type': 'application/x-ndjson'}, data = open('6test.json', 'rb'))
		print("Done!")
elastic()
