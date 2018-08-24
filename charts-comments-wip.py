# from bs4 import BeautifulSoup
import json
import requests

url = 'https://api-v2.soundcloud.com/charts?kind=top&genre=soundcloud%3Agenres%3Aall-music&high_tier_only=false&client_id=NZtb1cCBbHFHV67f1Fp9jkGKog0H4StA&limit=20&offset=0&linked_partitioning=1&app_version=1534947236&app_locale=en'

response = requests.get(url)
data = response.text
parsed = json.loads(data)

for list_item in parsed['collection']:
	track_id = list_item['track']['id']
	track_url = 'https://api-v2.soundcloud.com/tracks/' + str(track_id) + '/comments?threaded=0&filter_replies=1&client_id=NZtb1cCBbHFHV67f1Fp9jkGKog0H4StA&limit=10&offset=0&linked_partitioning=1&app_version=1534947236&app_locale=en'
	response2 = requests.get(track_url)
	data2 = response2.text
	comments = json.loads(data2)
	for comment in comments['collection']:
		print(comment['body'])
