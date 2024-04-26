import tempfile
import string
import os
import re
import math
import operator
from collections import defaultdict
from Common_IDF_Cal import inversefreq

'''
news_para_data = input("Enter the testing news:")
news_para_data.encode("utf8")
#news_para_data.encode("utf-8")
#news_para_data=news_para.encode("utf8")
# -----------------------Reading whole news----------------------------------------
#for news_detail in news_para_data:
print(news_para_data)
words_vector = []
semisport_vector = []
    # print(news_detail.string)


s = news_para_data

exclude = set(string.punctuation)
s = ''.join(ch for ch in s if ch not in exclude)
# print(s)
news = s.split(' ')
    # print(news)
for data in news:
    flag = 1
    text = open("stopword.txt", encoding="utf8").read()
    words_char = text.split("\n")
    # print(words_char)
    for each_word in words_char:
        if (data == each_word):
            flag = 0
            break;
        else:
            flag = 1
    if (flag == 1):
        words_vector.append(data)
            # print(data)
           # print(data,end=' ')
    # f.write(news_detail.string)
    # ------------------------------changes made hereeeee-------------------------------

    # print(words_vector)

text = open("noun.txt", encoding="utf8").read()
noun_vector = text.split("\n")
# print(noun_vector)

text = open("adjective.txt", encoding="utf8").read()
adjective_vector = text.split("\n")

text = open("adverb.txt", encoding="utf8").read()
adverb_vector = text.split("\n")

text = open("verb.txt", encoding="utf8").read()
verb_vector = text.split("\n")

for noun in noun_vector:
        # print(noun)
    for word in words_vector:
        if word.find(noun) != -1:
            # if str.__contains__(word, noun):
            if len(noun) != 1:
                semisport_vector.append(noun)
                # print(noun)
                break;

for adjective in adjective_vector:
    # print(noun)
    for word in words_vector:
        if word.find(adjective) != -1:
            # if str.__contains__(word, noun):
            if len(adjective) != 1:
                semisport_vector.append(adjective)
                # print(adjective)
                break;

for adverb in adverb_vector:
    # print(noun)
    for word in words_vector:
        if word.find(adverb) != -1:
            # if str.__contains__(word, noun):
            if len(adverb) != 1:
                semisport_vector.append(adverb)
                # print(adverb)
                break;

for verb in verb_vector:
    # print(noun)
    for word in words_vector:
        if word.find(verb) != -1:
            # if str.__contains__(word, noun):
            if len(verb) != 1:
                semisport_vector.append(verb)
                # print(verb)
                break;

print(semisport_vector)
print("***********************")
print(len(semisport_vector))

# ----------------------creating new document file and storing each semisport_vector in it----------------------------------------------------------
newfp = tempfile.NamedTemporaryFile(mode='a+', encoding="utf8", suffix='.txt',
                                    dir='G:\python projects\Crawler\TextTest', delete=False)
print(newfp.name)
for text_word in semisport_vector:
    newfp.write(text_word + ' ')

newfp.close()
'''
#--------------------------------calculate tfidf for test------------------------------------------------------------
DATA_PATH = "G:\python projects\Crawler\TextTest"

textdirs = os.listdir(DATA_PATH)  # returns list
texts = []
test_vector_space = {}
k = 1   # iterator to store subdictionary of test files in test_vector_space DIC.
# Loop over all of the files in the provided directory
for file in textdirs:

    # Ensure that only text files are included:
    if file.endswith(".txt"):
        text_dir = os.path.join(DATA_PATH, file)
        texts.append(text_dir)

#-------------------------------------------IDF calculations---------------------------------------------------------------
print("inverse freq dic in testnews file:")
print(inversefreq)
print(len(inversefreq))
#---------------------------------------------------------------------------------------------------------------------------

#----------------------------------------TF calculations--------------------------------------------------------------------------
for text in texts:
    print (text)
    with open(text, 'r', encoding="utf-8") as f:
        counts = defaultdict(int)
        num_words = 0
        for line in f:
            # Use Regex to remove punctuation and isolate words
            read_data = open(text, encoding="utf8").read()
            data = read_data.split(" ")
            print(len(data))
            num_words = len(data)
            for word in data:
                counts[word] += 1

    relativefreqs = {}
    tfidffreqs = {}
    for word, rawCount in counts.items():
        calfre = rawCount / num_words
        relativefreqs[word] = calfre

    # add this document's relative freqs to our dictionary
    del relativefreqs['']
    print(relativefreqs)
#-------------------------------------------- End TF calculation------------------------------------------------------------

#----------------------------------------------TF-IDF calculation------------------------------------------------------------
    test_vector_space[k] = {}
    for word ,calfre in relativefreqs.items():
        if word in inversefreq.keys():
            tfidf = relativefreqs[word] *inversefreq[word]
            tfidffreqs [word] = tfidf
            test_vector_space[k][word] = tfidffreqs[word]
    k += 1
print(test_vector_space[1])
print("the length of final test news vector space:")
print(len(test_vector_space[1]))
