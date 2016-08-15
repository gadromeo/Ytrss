import feedparser
import json
import urllib
import webbrowser

hot = feedparser.parse("http://www.billboard.com/rss/charts/hot-100")

print "================================"
print "=      BILLBOARD HOT 100       ="
print "================================"
print ""

#for x in range(0,len(hot['entries'])):
for x in range(0,25):
    #search = hot['entries'][x]['chart_item_title']
    print hot['entries'][x]['rank_this_week']+". "+hot['entries'][x]['chart_item_title']+" - "+hot['entries'][x]['artist']
    #results = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q="+search+"&type=video&key=AIzaSyCjTKZ7dY0oaTvbABEvPQ26nHkVaqnGtyE")
    #youjs = json.load(results)
    #print youjs['items'][0]['id']['videoId'] + ": " + youjs['items'][0]['snippet']['title']

print "0 to quit."
viewvid = int(raw_input('Watch video ranked #'))

if viewvid>100:
    viewvid = int(raw_input('Billboard only goes to 100! Watch video ranked #'))

while viewvid>0:
    search = hot['entries'][viewvid-1]['chart_item_title']
    results = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&order=date&q=gendarmerie%2Broyale&key=AIzaSyBNAkb86snLJdii_8XX2DZti2FBQ0xn8JE")
    youjs = json.load(results)
    print youjs['items'][0]['snippet']['title']
    webbrowser.open("https://www.youtube.com/watch?v="+youjs['items'][0]['id']['videoId'])
    viewvid = int(raw_input('Watch video ranked #'))
    if viewvid>100:
        viewvid = int(raw_input('Billboard only goes to 100! Watch video ranked #'))

#sdf
