# XKCD
TCMG 316 XKCD Project

----------ELASTICSEARCH XKCD INDEX MAPPING:----------

The scripts will not work without this xkcd mapping:

	PUT /xkcd
	{
		"settings": {
			"number_of_shards": 2,
			"number_of_replicas": 1,
			"analysis": {
				"filter": {
					"english_stop": {
						"type": "stop",
						"stopwords": "_english_"
					},
					"more_stop": {
						"type": "stop",
						"stopwords": ["shall", "from"]
					}
				},
				"analyzer": {
					"english": {
						"tokenizer": "standard",
						"filter": ["lowercase", "english_stop", "more_stop"]
					}
				}
			}
		},
		"mappings": {
				"properties": {
					"num": {
						"type": "keyword",
						"index": false
					},
					"link": {
						"type": "keyword",
						"index": false
					},
					"title": {
						"type": "keyword",
						"index": true
					},
					"safe_title": {
						"type": "keyword",
						"index": true
					},
					"alt": {
						"type": "keyword",
						"index": true
					},
					"img": {
						"type": "keyword",
						"index": false
					},
					"transcript": {
						"type": "text",
						"analyzer": "english",
						"term_vector": "with_positions_offsets",
						"index": true,
						"fielddata": true
					},
					"news": {
						"type": "text",
						"analyzer": "english",
						"term_vector": "with_positions_offsets",
						"index": true,
						"fielddata": true
					},
					"date": {
						"type": "date",
						"format": "yyyy-MM-dd"
					}
				}
			}
		}

----------CHANGES TO SCRIPTS:----------

In the xkcd_store.py script, replace these things with your information:
  
	Line 6, change the URL endpoint to match your URL endpoint from ElasticSearch. Leave the "/xkcd/_search?pretty" on the end.
		> Line 6  >   URL = "<paste your deployment's URL endpoint from Elasticsearch>/xkcd/_search?pretty"

	Line 17, change " 'elastic' " to your username for logging into your elastic DEPLOYMENT, not the same as logging into ElasticSearch. Do the same with " 'password' ".
      		> Line 17 >   response = requests.get(URL, data=query, auth=HTTPBasicAuth('elastic', 'password'), headers={'content-type': 'application/json'})

In the post.py script, replace the following items with your information:
  
  	Line 5, change the URL endpoint to match your URL endpoint from ElasticSearch. Leave the ' "/xkcd/_bulk" 'on the end.
      		> Line 5  >   ELASTIC_URL = "https://<Your URL Endpoint Here>/xkcd/_bulk"
  
	Line 7, change " 'elastic' " to your personal username for logging into your elastic deployment. Do the same with " 'password' ".
      		> Line 7  >   r = requests.post(ELASTIC_URL, auth=HTTPBasicAuth('elastic', 'password'), headers = {'content-type': 'application/x-ndjson'}, data = open('6test.json', 'rb'))

In the search.py script, replace the following items with your information:
  
	Line 4, change the URL endpoint to match your URL endpoint from ElasticSearch. Leave the ' "/xkcd/_search?q=" 'on the end.
      		> Line 4  >   URL = "https://<Your URL Endpoint Here>/xkcd/_search?q="
  
	Line 11, change " 'elastic' " to your personal username for logging into your elastic deployment. Do the same with " 'password' ".
      		> Line 11 >   search = requests.get(url = URL + word, auth = HTTPBasicAuth('elastic', 'password'))
    
Directions for after you have downloaded each file, and have made the apporpriate changes to the files to fit your personal information:

	First, run xkcd_store.py, this will take a couple minutes. Then run post.py to post all of the json data into elasticsearch. Then you can run search.py to search for a comic. Enjoy!
