#!/usr/bin/env python
"""mapper.py"""

import sys
import string

# top words for News data

#top_words = ['trump','clinton','hillary','fisa','application','campaign','dossier','spy','funded','report']


#top ten words for NYT_elections
#top_words= ['election','government','dowless','voters','party','political','people','years','president','state']
#top ten words for NYT_goverons
#top_words=['trump','cohen','government','president','house','michael','people','american','states','company']
#top ten words for NYT_politicalparty
#top_words=['party','election','trump','political','democrats','president','new','voters','democratic','politics']
#top ten words for NYT_vote
#top_words=['democrats','vote','political','house','resolution','european','brexit','republican','president','party']\
#top ten words for NYT_trump
top_words=['trump','president','cohen','said', 'michael','would','new','people','bank','mueller']

#top ten words for Common_crawl
#top_words= ['election','trump','president','elections','state','party','vote','states','house','india']


#top_ten words for Twitter_trump_hilary
#top_words=['trump','clinton','hillary','fisa','application','campaign','dossier','spy', 'funded','report']

#top_ten words for Twitter political_party
#top_words=['party','political','people','one','democrats','like','sad','excuse','trump','country']

#top_ten words for Twitter goveron
#top_words=['government','border','people','trump','president','new','children','citizens','medical','experiments']

#top_ten words for Twitter elections
#top_words=['elections','vote','new','presidential','electoral','popular','mexico','bill','college','voters']

#top_ten words for Twitter vote
#top_words=['vote','crisis','right','congress','president','party','year','trump','want','open']

for ipdata in sys.stdin:
        ipdata = ipdata.strip()
       # split the line into words
        words = ipdata.split()
	
	for i in range(len(words)-1):
		x = words[i]
		if x in top_words:
			print ("<"+x+","+ words[i+1]+">\t"+str(1))



