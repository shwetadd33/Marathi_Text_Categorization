from math import *
from tfidf import *
from testnews import *
import collections

print("--------------------------------TESTING SECTION------------------------------------------------")
print("Test vector space:")
print(test_vector_space)
print(len(test_vector_space))

i=1
jaccard_similarity_dic = {}

print ("*******************************************")
print(total_traindata)
while i <= total_traindata:
    intersection_count = 0
    for word,frequency in test_vector_space.items():
        if univerdsal_vector_space[i][word] != 0:
            intersection_count += 1

    jaccard_similarity_dic[i] = intersection_count/len(test_vector_space)
    i += 1

print("jaccard similarity dic is:")
print(jaccard_similarity_dic)
print(len(jaccard_similarity_dic))

sorted_jaccardsim_dic = collections.OrderedDict(sorted(jaccard_similarity_dic.items(), key=operator.itemgetter(1)))
print("Sorted jaccard_similarity_dic is:")
print(sorted_jaccardsim_dic)
print(len(sorted_jaccardsim_dic))


for k, v in sorted_jaccardsim_dic.items():
    if k <= m:
        print("sport")
    elif m < k <= m+n:
        print("enter")
    else:
        print("eco")


'''for keyvalue in euclidean_distance_dic:
    print("key value is")
    print(euclidean_distance_dic[keyvalue])'''

