import json
import urllib

search = raw_input('search term')

results = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&order=date&q=gendarmerie%2Broyale&key=AIzaSyBNAkb86snLJdii_8XX2DZti2FBQ0xn8JE")
youjs = json.load(results)
print youjs['items'][0]['id']
print youjs['items'][0]['snippet']['title']
#json.load("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=maple%20story&type=video&key=AIzaSyCjTKZ7dY0oaTvbABEvPQ26nHkVaqnGtyE")
