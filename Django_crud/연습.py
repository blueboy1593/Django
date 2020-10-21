import requests
from pprint import pprint



url = 'http://api.giphy.com/v1/gifs/search?api_key=4i1aScgdTDrEGFZuIltFlaHACRS0QWA6&q=경찰&limit=1'
url2 = ''

data = requests.get(url).json()
new_url = data['data'][0]['images']['downsized']['url']
pprint(data['data'][0]['images']['downsized']['url'])