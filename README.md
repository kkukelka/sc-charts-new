# sc-charts: Soundcloud charts web scraper

## Getting started
The scripts provided allow the collection of various kinds of data from [Soundcloud Charts - Top 50](https://soundcloud.com/charts/top).
- __top20-meta.py__ can be used to collect meta data such as 'artist', 'genre', 'likes' in an organized .csv file. When using the script, a dump-folder is created in the current directory. Each sample is timestamped with regards to your current location.
- __charts-comments.py__ can be used to extract comments from all chart items; future functionality will include writing to csv and specifying comments per track (currently work in progress)