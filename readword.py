import re

#separators = [u"।", u",", u"."]
'''
text = open("stopword.txt",encoding="utf8").read()
#This converts the encoded text to an internal unicode object, where
# all characters are properly recognized as an entity:
#text = text.decode("utf-8")

#this breaks the text on the white spaces, yielding a list of words:
words = text.split("\n")

text1 = open("stopword2.txt", encoding="utf8").read()
words_1 = text1.split("\n")

#counter = 1

#output = ""
for word1 in words_1:
    flag = 0
    #if the last char is a separator, and is joined to the word:
    #output += word + u" "
    for word in words:
        if(word1==word):
            flag = 1
            break;
        else:
            flag = 0
    if(flag==0):
        f = open("stopword.txt", "a+", encoding="utf8")
        f.write(word1)
        f.write("\n")
        f.close()
'''
'''
text1 = open("train.txt",encoding="utf8").read()
words_vector = text1.split(" ")
#print(words_vector)

text = open("noun.txt",encoding="utf8").read()
noun_vector = text.split("\n")
#print(noun_vector)

text = open("adjective.txt",encoding="utf8").read()
adjective_vector = text.split("\n")

text = open("adverb.txt",encoding="utf8").read()
adverb_vector = text.split("\n")

text = open("verb.txt",encoding="utf8").read()
verb_vector = text.split("\n")


for noun in noun_vector:
    #print(noun)
    for word in words_vector:
        if word.find(noun) != -1 :
        #if str.__contains__(word, noun):
            if len(noun) != 1:
                print(noun)
                break;

for adjective in adjective_vector:
    #print(noun)
    for word in words_vector:
        if word.find(adjective) != -1 :
        #if str.__contains__(word, noun):
            if len(adjective) != 1:
                print(adjective)
                break;

for adverb in adverb_vector:
    #print(noun)
    for word in words_vector:
        if word.find(adverb) != -1 :
        #if str.__contains__(word, noun):
            if len(adverb) != 1:
                print(adverb)
                break;

for verb in verb_vector:
    #print(noun)
    for word in words_vector:
        if word.find(verb) != -1 :
        #if str.__contains__(word, noun):
            if len(verb) != 1:
                print(verb)
                break;
'''
'''for each_word in words_char:
    l = len(each_word)
    print(l)
    char_list = list(each_word)
    #joining = ' '.join(char_list)
    print("\n")
    for char in char_list:
            print(char, end=' ')
'''

depth = [[]]

for i in range(4):
    depth.append([])

depth[1].append("shweta")
print(depth[1])
print(depth[3])