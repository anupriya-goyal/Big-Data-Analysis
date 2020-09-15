# Big-Data-Analysis
Project related to analysis of data collected from Twitter, NYT, Common Crawl
#
## Topic of Data collection:
Data is collected on politics “Politics”. <br/>
<br/>
### DATA SETS:
        Collected large amount of data sets from 3 different sources:<br/>
        ● Twitter
        ● New York Times
        ● Common Crawls 
### WORDS USED FOR DATA COLLECTION:
        ● Trump or Hilary 
        ● Elections 
        ● Government 
        ● Vote 
        ● Political party 
        Used the same set of words to collect data from all 3 data sources: Twitter, New York Times 
        and Common Crawls.
        
### STEPS FOLLOWED :
        ● Initially, we took data from Twitter using Twitter API and ‘rtweet’ package in R using
          the script file- ‘Tweets_collection.ipynb’.
        ● Then we collected data from New York Times using New York Times API . We have
          used the following script file for that- ‘ NYT_collection.ipynb’.
        ● Then we took data from Common Crawls using commoncrawl.org, where we downloaded selected 
          latest march 2019 data, and then downloaded .WET files , crawled manually searching keywords 
          and saved the relevant text and URLs.
        ● We collected the data for the period between Feb 1, 2019 to April 15, 2019.
        ● We cleaned the data, by performing lemmatization, then removed stop words and punctuations, 
          then written to text file named according to the keyword and data source.
        ● That cleaned text file is input to the Mapper Class where we perform word count
          functionality and output the valid word and count as < word,1>
