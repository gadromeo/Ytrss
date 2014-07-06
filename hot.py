import feedparser
import json
import urllib

hot = feedparser.parse("http://www.billboard.com/rss/charts/hot-100")

print "==============================="
print "=      BILLBOARD HOT 100      ="
print "==============================="
print ""

#for x in range(0,len(hot['entries'])):
for x in range(0,5):
    search = hot['entries'][x]['chart_item_title']
    print hot['entries'][x]['rank_this_week']+". "+hot['entries'][x]['chart_item_title']+" - "+hot['entries'][x]['artist']
    results = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q="+search+"&type=video&key=AIzaSyCjTKZ7dY0oaTvbABEvPQ26nHkVaqnGtyE")
    youjs = json.load(results)
    print youjs['items'][0]['id']['videoId'] + ": " + youjs['items'][0]['snippet']['title']
