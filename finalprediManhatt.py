from math import *
from tfidf import *
from testnews import *
import collections

print("--------------------------------TESTING SECTION------------------------------------------------")
print("Test vector space:")
print(test_vector_space)
print(len(test_vector_space))

i=1
manhatt_distance_dic = {}

print ("*******************************************")
print(total_traindata)
while i <= total_traindata:
    manhatt_distance = 0
    for word,frequency in test_vector_space.items():
        if word in univerdsal_vector_space[i].keys():
            manhatt_distance += abs(test_vector_space[word] - univerdsal_vector_space[i][word])
    manhatt_distance_dic[i] = manhatt_distance
    i += 1

print("cosine similarity dic is:")
print(manhatt_distance_dic)
print(len(manhatt_distance_dic))

sorted_manhattdist_dic = collections.OrderedDict(sorted(manhatt_distance_dic.items(), key=operator.itemgetter(1)))
print("Sorted euclidean_distance_dic is:")
print(sorted_manhattdist_dic)
print(len(sorted_manhattdist_dic))


for k, v in sorted_manhattdist_dic.items():
    if k <= m:
        print("sport")
    elif m < k <= m+n:
        print("enter")
    else:
        print("eco")


'''for keyvalue in euclidean_distance_dic:
    print("key value is")
    print(euclidean_distance_dic[keyvalue])'''

