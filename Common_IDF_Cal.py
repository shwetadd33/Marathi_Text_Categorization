import os
import csv
import string
import re
import math
import operator
from collections import defaultdict

texts = []                #text : list used for storing whole path of training files of all the categories
i =  1
#--------------------------SPORTS-----------------------------------------------
DATA_PATH_SPORT = "G:\python projects\Crawler\Text"

textdirs_sport = os.listdir(DATA_PATH_SPORT)  # returns list

# Loop over all of the files in the provided directory
for file in textdirs_sport:
    # Ensure that only text files are included:
    if file.endswith(".txt"):
        text_dir = os.path.join(DATA_PATH_SPORT, file)
        texts.append(text_dir)

m = len(texts)    #m: Iterator for number of files in sports file directory


#--------------------------ENTERTAINMENT-----------------------------------------------
DATA_PATH_ENTER = "G:\python projects\Crawler\TextEnter"

textdirs_enter = os.listdir(DATA_PATH_ENTER)  # returns list
# Loop over all of the files in the provided directory
for file in textdirs_enter:

    # Ensure that only text files are included:
    if file.endswith(".txt"):
        text_dir = os.path.join(DATA_PATH_ENTER, file)
        texts.append(text_dir)

n = len(texts) - m    #n: Iterator for number of files in enterainment file directory


#--------------------------ECONOMY-----------------------------------------------
DATA_PATH_ECO = "G:\python projects\Crawler\TextEconoy"

textdirs_eco = os.listdir(DATA_PATH_ECO)  # returns list
# Loop over all of the files in the provided directory
for file in textdirs_eco:

    # Ensure that only text files are included:
    if file.endswith(".txt"):
        text_dir = os.path.join(DATA_PATH_ECO, file)
        texts.append(text_dir)

l = len(texts) - m - n   #l: Iterator for number of files in enterainment file directory

#----------------------------------------------------------------------------------------

universal_dic = {}

for text in texts:
    with open(text, 'r', encoding="utf-8") as f:
        counts = defaultdict(int)
        num_words = 0

        for line in f:
            # Use Regex to remove punctuation and isolate words
            read_data = open(text, encoding="utf8").read()
            data = read_data.split(" ")
            num_words = len(data)

            for word in data:
                counts[word] += 1

        for word in counts.keys():
            if word in universal_dic.keys():
                universal_dic[word] +=1
            else:
                universal_dic[word] = 1
        #universal_dic.update(counts)
print(universal_dic)
#del universal_dic['']
print(universal_dic)

#-------------------------------------------IDF calculations---------------------------------------------------------------
inversefreq = {}
for word, wordCount in universal_dic.items():
    invfre = 1 + math.log(len(texts)/wordCount)
    inversefreq[word] = invfre

print("inverse freq dic in Common_IDF_Cal file:")
print(inversefreq)
print(len(inversefreq))

#----------------------------------------IDF calculation ends---------------------------------------------------------------------
