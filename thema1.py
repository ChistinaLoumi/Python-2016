import urllib2
import json
title=raw_input("Enter the title of the movie you are looking for:")
x= "http://www.omdbapi.com/?t="+title+"&y=&plot=short&r=json"  
url=x  
request = urllib2.Request(url)
handle = urllib2.urlopen(request)
tainia = handle.read()

print tainia 
#PROSPATHISA NA TO XWRISW KAI NA PARV TA DEDOMENA ALLA DEN MOY DOYLEYE ME TIPOTA