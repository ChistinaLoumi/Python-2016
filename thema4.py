import urllib2
import json
#dinei o xrhsths thn tainia
title=raw_input("Enter the title of the movie you are looking for:")
url= "http://www.omdbapi.com/?t="+title+"&y=&plot=short&r=json"  
 #syndew thn istoselida me to programma
response = urllib2.urlopen(url)
#metatrepw ta stoixeia
data = json.loads(response.read())
#tatata...na to apotelesma
print "the IMBD score is:"+data["imdbRating"]
print "Awards:"+data["Awards"]
