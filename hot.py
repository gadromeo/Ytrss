import feedparser

hot = feedparser.parse("http://www.billboard.com/rss/charts/hot-100")

print "==============================="
print "=      BILLBOARD HOT 100      ="
print "==============================="
print ""

for x in range(0,len(hot['entries'])):
    print hot['entries'][x]['rank_this_week']+". "+hot['entries'][x]['chart_item_title']+" - "+hot['entries'][x]['artist']
