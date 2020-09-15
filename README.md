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
        ● Initially, collected the data from Twitter using Twitter API and ‘rtweet’ package in R using
          the script file- ‘Tweets_collection.ipynb’.
        ● Then collected data from New York Times using New York Times API .We have used the following 
          script file for that- ‘ NYT_collection.ipynb’.
        ● Then we took data from Common Crawls using commoncrawl.org, where we downloaded selected 
          latest march 2019 data, and then downloaded .WET files , crawled manually searching keywords 
          and saved the relevant text and URLs.
        ● Collected the data for the period between Feb 1, 2019 to April 15, 2019.
        ● Cleaned the data, by performing lemmatization, then removed stop words and punctuations, 
          then written to text file named according to the keyword and data source.
        ● That cleaned text file is input to the Mapper Class where we perform word count
          functionality and output the valid word and count as < word,1>
        ● In the Reducer, we sum the value part of each word from all mappers and get the count of
          words and output <word, count>.
        ● We then use this output to generate word cloud to depict data using interactive
          visualization Tableau.
### WEBSITE/ PUBLISHED URL:
        https://public.tableau.com/profile/anupriya.goyal?/vizhome/Workbook1_15558769608410/Twitter_all_word_co#!/  
       
         ● From the visualization it is found that ‘Trump’, is the highest count word for both Twitter and 
           New York Times but for Common Crawl it is ‘Election’ with count 384 and
          ‘Trump’ with count 380.
        ● Then we are sorting the word-count pairs by value with sorting.ipynb and use the top 10 words from 
          the sorted data to find the co-occurrence words.
        ● We found the co-occurrence words using a Map Reduce method for Twitter, New York Times and 
          Common Crawl separately.
        ● In the Mapper, used the Top 10 words from the sorted collection for Twitter, New York Times and 
          Common Crawls data and we generate a key-value pair and output it to
          file.
        ● So, the output of the mapper will be of the form ( {word co-occurrence}, 1).
        ● In the Reducer, used the output from the Mapper and reduce it to get the count of the
          co-occurrence word.
        ● The output of the Reducer will be of the form ( {word co-occurrence}, count).
        ● For visualizing the co-occurrence generated the word cloud from Tableau .
         
