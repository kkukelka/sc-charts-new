#BLUEPRINT FOR JSON API RESPONSE SCRAPING

import json
import requests
import csv
import time
import os

url = 'https://api-v2.soundcloud.com/charts?kind=top&genre=soundcloud%3Agenres%3Aall-music&high_tier_only=false&client_id=rZY6FYrMpGVhVDfaKEHdCaY8ALekxd8P&limit=20&offset=0&linked_partitioning=1&app_version=1534496081&app_locale=en'
r = requests.get(url)
# or 'response = requests.get(url)'

json_data = r.json()
collection = json_data['collection']

# creates dump-folder in current directory
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, 'top20-samples')
if not os.path.exists(final_directory):
	os.makedirs(final_directory)

# creates a timestamp for the csv-file
current_time = time.strftime('%m.%d.%y-%H%MPM.csv', time.localtime())
logname = 'top20-sample_' + '%s' % current_time
file_name = ''.join(logname)

# creates csv file with timestamp in dump-folder
with open(f'{final_directory}/{file_name}', 'w', encoding='utf-8') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(
		['Artist', 'Title', 'Genre', 'Label', 'Likes', 'Comments', 'Plays'])

	for d in collection:
		artist = d['track']['user']['username']
		title = d['track']['title']
		genre = d['track']['genre']
		label = d['track']['label_name']
		likes = d['track']['likes_count']
		cc = d['track']['comment_count']
		plays = d['track']['playback_count']
		csv_writer.writerow([artist, title, genre, label, likes, cc, plays])
