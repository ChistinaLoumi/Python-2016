import urllib2
import json
import datetime
i = datetime.datetime.now()
date= i.strftime('%d-%m-%Y')#pairnw tin hmeromhnia apo to systhma
url=" http://applications.opap.gr/DrawsRestServices/kino/drawDate/"+date+".json"#vazw thn hmeromhnia sto url
response = urllib2.urlopen(url)


dedomena = handle.read()

print dedomena
#den mporv me tipota ta stoixeia tou tuple na ta balw se mia lista 