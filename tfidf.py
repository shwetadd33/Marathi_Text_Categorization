import os
import csv
import string
import re
import math
import operator
from collections import defaultdict
import collections
from testnews import *

texts = []                #text : list used for storing whole path of training files of all the categories
counter = 1
sport_categorized = 0
enter_categorized = 0
eco_categorized = 0

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
for k in range(1,len(test_vector_space)+1):
    universal_dic = {}
    univerdsal_vector_space = {}  #univerdsal_vector_space: This dictionary is used for storing sub dictionaries of "text" list. Sub-dictionary:is storing the TF-IDf calculation for that textfile(doc) w.r.t "Test document".
    i = 1
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
    #print(universal_dic)
    #del universal_dic['']
    #print(universal_dic)

    #-------------------------------------------IDF calculations---------------------------------------------------------------
    inversefreq = {}
    for word, wordCount in universal_dic.items():
        invfre = 1 + math.log(len(texts)/wordCount)
        inversefreq[word] = invfre

    #print("inverse freq dic:")
    #print(inversefreq)
    #print(len(inversefreq))

    #----------------------------------------IDF calculation ends---------------------------------------------------------------------

    #----------------------------------------TF calculations--------------------------------------------------------------------------
    for text in texts:
        with open(text, 'r', encoding="utf-8") as f:
            counts = defaultdict(int)
            num_words = 0
            for line in f:
                # Use Regex to remove punctuation and isolate words
                read_data = open(text, encoding="utf8").read()
                data = read_data.split(" ")
                #print(len(data))
                num_words = len(data)
                for word in data:
                    counts[word] += 1

        relativefreqs = {}
        tfidffreqs = {}
        for word, rawCount in counts.items():
            #print (rawCount)
            #relativefreqs[word] = rawCount #/ num_words
            # gather only words with alphabetical characters, discard ones with numbers
            calfre = rawCount / num_words
            #cal = round(calfre,8)
            relativefreqs[word] = calfre

        # add this document's relative freqs to our dictionary
        #del relativefreqs['']
        #print("Relative frequecy vector for current text file")
        #print(relativefreqs)
    #-------------------------------------------- End TF calculation------------------------------------------------------------

    #----------------------------------------------TF-IDF calculation------------------------------------------------------------
        univerdsal_vector_space[i] = {}
        for word ,calfre in test_vector_space[k].items():
            if word in relativefreqs.keys():
                tfidf = relativefreqs[word] * inversefreq[word]
            else:
                tfidf = 0

            tfidffreqs[word] = tfidf
            univerdsal_vector_space[i][word] = tfidffreqs[word]
        i = i + 1

    #print("----------The Universal Vector Space Is--------- ")
    #print(univerdsal_vector_space)
    #print("the length of final sport vector space:")
    #print(len(univerdsal_vector_space))

    '''
    print("----------The test Vector Space Is--------- ")
    print(test_vector_space)
    print(len(test_vector_space))

    print("----------The 1st Vector Space Is--------- ")
    print(univerdsal_vector_space[1])
    print(len(univerdsal_vector_space[1]))

    print("----------The 2nd Vector Space Is--------- ")
    print(univerdsal_vector_space[2])
    print(len(univerdsal_vector_space[2]))

    print("----------The 2nd Vector Space Is--------- ")
    print(univerdsal_vector_space[260])
    print(len(univerdsal_vector_space[260]))
    

    print(texts)
    print(len(texts))
    '''
    total_traindata = m + n + l
    '''
    print("value of m:")
    print(m)

    print("value of n:")
    print(n)

    print("value of l:")
    print(l)

    print("inverse freq dic in tfidf file:")
    print(inversefreq)
    print(len(inversefreq))
    '''
    print("--------------------------------TESTING SECTION------------------------------------------------")

    i_eucli = 1
    euclidean_distance_dic = {}
    sport_count = 0
    enter_count = 0
    eco_count = 0
    count_word = []
    #print("*******************************************")
    #print(total_traindata)
    while i_eucli <= total_traindata:
        distance = 0
        for word, frequency in test_vector_space[k].items():
            if word in univerdsal_vector_space[i_eucli].keys():
                distance += pow(univerdsal_vector_space[i_eucli][word] - test_vector_space[k][word], 2)
        eucli_distance = math.sqrt(distance)
        euclidean_distance_dic[i_eucli] = eucli_distance
        i_eucli += 1

    #print("euclidean_distance_dic is:")
    #print(euclidean_distance_dic)
    #print(len(euclidean_distance_dic))

    sorted_euclidist_dic = collections.OrderedDict(sorted(euclidean_distance_dic.items(), key=operator.itemgetter(1)))
    #print("Sorted euclidean_distance_dic is:")
    #print(sorted_euclidist_dic)
    #print(len(sorted_euclidist_dic))
    main_count = 0
    for k, v in sorted_euclidist_dic.items():
        if k <= m:
            sport_count += 1
            #print("sport")
        elif m < k <= m + n:
            enter_count += 1
            #print("enter")
        else:
            eco_count += 1
            #print("eco")
        main_count += 1

        if main_count >= math.sqrt(total_traindata):
            break;
    count_word.append(sport_count)
    count_word.append(enter_count)
    count_word.append(eco_count)
    print("List count_word is:")
    print(count_word)

    index = count_word.index(max(count_word))

    if index == 0:
        print("SPORTS")
        sport_categorized += 1
    elif index == 1:
        print("ENTERTAINMENT")
        enter_categorized += 1
    else:
        print("ECONOMICAL AFFAIRS")
        eco_categorized += 1
    '''for keyvalue in euclidean_distance_dic:
        print("key value is")
        print(euclidean_distance_dic[keyvalue])'''

print("Total news categorized as SPORT category:")
print(sport_categorized)

print("Total news categorized as ENTERTAINMENT category:")
print(enter_categorized)

print("Total news categorized as ECONOMY category:")
print(eco_categorized)
