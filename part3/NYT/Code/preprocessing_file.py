# -*- coding: utf-8 -*-

import sys
import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import nltk.data
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import RegexpTokenizer
import io 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
nltk.download('stopwords')
import os

nltk.download('wordnet')

#Give file name according of unproceesed files collected in part1 for Twitter, NYT and Common crawl
#lemmitization
lemmatizer = WordNetLemmatizer()
file=open("part1/Twitter/Data/filename.txt")
my_lines_list=file.readlines()
my_lines_list

#print(my_lines_list[0])
print("Stemmed sentence")
for i in range (0,len(my_lines_list)):
        x=lemmatizer.lemmatize(my_lines_list[i])
        appendFile = open('/content/gdrive/My Drive/Colab Notebooks/lemiz_test_new.txt','a') 
        appendFile.write(" "+x) 

        #print(x)
appendFile.close() 

#removal of @, & and http and stop words
import re
stop_words = set(stopwords.words('english')) 
file1 = open("lemiz_test_new.txt",encoding="utf8") 
line = file1.read()
#print(line)
result = re.sub(r"http\S+", "", line)
result1=re.sub('#\S+','',result)
result2=re.sub('@\S+','',result1)
result3=re.sub('<\S+','',result2)
result4=re.sub('&\S+','',result3)

appendFile = open('removal_http_other_new.txt','a') 
appendFile.write(" "+result4) 
#print(result4)
appendFile.close() 


file2 = open("removal_http_other_new.txt") 
line1 = file2.read()
    
words =line1.split()  
#print(words)
for r in words: 
            #print(r)
            top_words = nltk.corpus.stopwords.words('english')
            #print(top_words)
            data_lower = r.lower();
            #print(data_lower)

            tokenizer = RegexpTokenizer(r'\w+')
            word_list = tokenizer.tokenize(data_lower)
            for x in word_list:
                if x not in stop_words and x.isalpha() and len(x)>2:
                    #print(r)
                    appendFile = open('Twitter_political_party_preprocessed.txt','a') 
                    appendFile.write(" "+x) 
                    #print(x)
                    appendFile.close()
        

os.remove('removal_http_other_new.txt')
os.remove('lemiz_test_new.txt')

