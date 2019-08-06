# The program to sort by count and get top 10 words for word co-occurrence.
d = {}
with open("NYT_vote_word_co",encoding='latin-1') as f:
    for line in f:
        (key, val) = line.split()
        d[(key)] = val
        
dict_with_ints = dict((k,int(v)) for k,v in d.items())

top_ten=(sorted(dict_with_ints.items(), key = lambda kv:(kv[1], kv[0]), reverse =True)[:10])
print(top_ten)
top_fifty=(sorted(dict_with_ints.items(), key = lambda kv:(kv[1], kv[0]), reverse =True)[:50])
top_hundred=(sorted(dict_with_ints.items(), key = lambda kv:(kv[1], kv[0]), reverse =True)[:100])
#print(top_ten)

with open('ten_NYT_vote_word_co.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in top_ten))
with open('fifty_NYT_vote_word_co.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in top_fifty))
    
with open('hundred_NYT_vote_word_co.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in top_hundred))
    
     
#os.remove('/content/gdrive/My Drive/Colab Notebooks/Top_ten_NYT/part1')

####################Twittwer_com#################
#Top_ten_twitter_all_word_count

#[('trump', 10894), ('clinton', 9649), ('hillary', 4724), ('vote', 3722), ('fisa', 3641), ('application', 3117), ('party', 2734), ('campaign', 2569), ('president', 2565), ('political', 2547)]
#Top_ten_twitter_all_word_co

#[('<hillary,clinton>', 4496), ('<fisa,application>', 3117), ('<trump,campaign>', 1983), ('<clinton,funded>', 1947), ('<application,used>', 1557), ('<application,fisa>', 1557), ('<president,trump>', 1297), ('<political,party>', 1242), ('<trump,poll>', 1074), ('<clinton,illegally>', 1074)]

############# NYT_com#####################
#Top_ten_NYT_all_word_count
#[('trump', 1927), ('said', 1901), ('president', 987), ('would', 878), ('new', 841), ('party', 757), ('cohen', 712), ('election', 695), ('one', 679), ('people', 674)]

#Top_ten_NYT_all_word_co
#[('<new,york>', 294), ('<president,trump>', 175), ('<trump,organization>', 72), ('<cohen,said>', 64), ('<new,election>', 53), ('<new,deal>', 52), ('<said,would>', 45), ('<trump,administration>', 41), ('<said,statement>', 34), ('<trump,said>', 32)]

#top Ten words for NYT_elections
    
#('election', 372), ('government', 324), ('dowless', 213), ('voters', 205), ('party', 192), ('political', 149), ('people', 146), ('years', 136), ('president', 134), ('state', 132)


#top Ten words_ cooccurence for NYT_elections
#('<election,fraud>', 22), ('<election,commission>', 17), ('<election,day>', 11), ('<state,board>', 10), ('<political,operative>', 10), ('<president,trump>', 9), ('<political,scientist>', 9), ('<state,officials>', 8), ('<political,science>', 8), ('<political,parties>', 8)]

#top Ten words for NYT_goveron
#('trump', 446), ('cohen', 295), ('government', 213), ('president', 201),('house', 131), ('michael', 130),('people', 124), ('american', 107), ('states', 90),('company', 87)
#Top ten words for NYT_goveron

#('<michael,cohen>', 92), ('<president,trump>', 40),('<american,officials>', 26), ('<house,oversight>', 22), ('<trump,administration>', 20), ('<house,counsel>', 11), ('<cohen,testimony>', 11), ('<trump,organization>', 10), ('<michael,barbaroand>', 8), ('<cohen,testified>', 8)
#top Ten words for NYT_politicalparty_word_count

#('party', 365), ('election',348), ('trump', 275), ('political', 195), ('democrats', 177), ('president', 170), ('new', 159), ('voters', 119), ('democratic', 148), ('politics', 146)]

#Top_ten words for NYT_politicalparty_word_co
#('<party,leader>', 36), ('<president,trump>', 30), ('<democratic,party>', 29), ('<new,deal>', 26), ('<election,commission>', 13), ('<political,scientist>', 11), ('<voters,percent>', 10), ('<political,parties>', 10), ('<democratic,candidates>', 10), ('<democratic,primary>', 9)]


#Top_ten words for NYT_vote_word_count
#('democrats', 487), ('vote', 272), ('political', 229), ('house', 178),('resolution', 168),('european', 150), ('brexit', 162), ('republican', 146), ('president', 142), ('party', 134)]

#Top_ten words for NYT_vote_word_co
#('<european,union>', 60), ('<president,trump>', 25), ('<resolution,disapproval>', 12), ('<house,democrats>', 12), ('<republican,senators>', 11), ('<vote,resolution>', 8), ('<brexit,supporters>', 7), ('<brexit,process>', 7), ('<brexit,hard>', 7), ('<brexit,deal>', 7)]



#Top_ten words for NYT_trump_word_count
#[('trump', 1027), ('president', 392), ('cohen', 292), ('said', 287), ('michael', 235), ('would', 208), ('new', 192), ('people', 156), ('bank', 156), ('mueller', 155)]

#Top_ten words for NYT_trump_word_co
#[('<new,york>', 129), ('<michael,cohen>', 93), ('<president,trump>', 71), ('<trump,organization>', 65), ('<cohen,said>', 30), ('<trump,campaign>', 21), ('<said,trump>', 19), ('<mueller,report>', 19), ('<trump,said>', 18), ('<trump,tower>', 17)]


###########Common Crawl #################

# top ten of common crawl word count
#[('election', 384), ('trump', 380), ('president', 280), ('elections', 263), ('state', 221), ('party', 181), ('vote', 178), ('states', 168), ('house', 166), ('india', 153)]

#top ten of common crawl word co
#[('<president,donald>', 51), ('<house,representatives>', 30), ('<president,trump>', 28), ('<election,commission>', 23), ('<election,day>', 21), ('<party,bjp>', 16), ('<elections,clause>', 14), ('<president,united>', 13), ('<india,general>', 12), ('<house,senate>', 12)]



######### Twitter###########

#top ten trump_hilary_word_count
#[('trump', 10083), ('clinton', 9594), ('hillary', 4656), ('fisa', 3633), ('application', 3117), ('campaign', 2457), ('dossier', 2103), ('spy', 1959), ('funded', 1956), ('report', 1932)]

#top ten trump_hilary_word_co
#[('<hillary,clinton>', 4473), ('<fisa,application>', 3117), ('<trump,campaign>', 1974), ('<clinton,funded>', 1947), ('<spy,trump>', 1944), ('<report,made>', 1560), ('<funded,dossier>', 1557), ('<dossier,get>', 1557), ('<application,used>', 1557), ('<application,fisa>', 1557)]

#top ten_political_party_word_count
#[('party', 2229), ('political', 2149), ('people', 292), ('one', 225), ('democrats', 210), ('like', 194), ('sad', 193), ('excuse', 189), ('trump', 151), ('country', 134)]


#top ten_political_party_word_co
#[('<political,party>', 1221), ('<sad,excuse>', 166), ('<excuse,political>', 152), ('<democrats,sad>', 76), ('<political,parties>', 72), ('<party,political>', 47), ('<one,political>', 47), ('<political,partyâ>', 44), ('<party,country>', 39), ('<political,system>', 29)]

#top ten_goveron_word_count
#[('government', 2108), ('border', 402), ('people', 339), ('trump', 251), ('president', 228), ('new', 225), ('children', 224), ('citizens', 214), ('medical', 197), ('experiments', 194

#top ten_goveron_word_co
#[('<medical,experiments>', 188), ('<government,medical>', 186), ('<experiments,brown>', 185), ('<children,stole>', 185), ('<president,trump>', 150), ('<people,arenâ>', 146), ('<government,benefits>', 146), ('<citizens,new>', 146), ('<border,wall>', 146), ('<trump,cut>', 145)]

#top ten_elections_word_count

#[('elections', 1982), ('vote', 646), ('new', 401), ('presidential', 381), ('electoral', 381), ('popular', 369), ('mexico', 361), ('bill', 327), ('college', 316), ('voters', 294)]

#top ten_elections_word_co
#[('<presidential,elections>', 373), ('<popular,vote>', 364), ('<new,mexico>', 335), ('<electoral,college>', 310), ('<vote,electoral>', 289), ('<elections,popular>', 286), ('<bill,decide>', 283), ('<mexico,governor>', 282), ('<elections,canada>', 132), ('<voters,vote>', 126)]


#top ten_vote_word_count
#[('vote', 2798), ('crisis', 404), ('right', 356), ('congress', 315), ('president', 300), ('party', 297), ('year', 252), ('trump', 246), ('want', 244), ('open', 242)]


#top ten_vote_word_co
#[('<vote,right>', 228), ('<open,vote>', 227), ('<vote,congress>', 203), ('<president,cynically>', 201), ('<congress,perpetuate>', 201), ('<crisis,challenges>', 187), ('<year,olds>', 94), ('<right,vote>', 93), ('<year,unions>', 90), ('<want,year>', 90)]









