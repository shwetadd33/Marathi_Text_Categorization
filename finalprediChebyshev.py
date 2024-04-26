from math import *
from tfidf import *
from testnews import *
import collections

print("--------------------------------TESTING SECTION------------------------------------------------")
print("Test vector space:")
print(test_vector_space)
print(len(test_vector_space))

i=1
chebyshev_distance_dic = {}

print ("*******************************************")
print(total_traindata)
while i <= total_traindata:
    max_chebyshev_distance = 0
    for word,frequency in test_vector_space.items():
        if word in univerdsal_vector_space[i].keys():
            chebyshev_distance = abs(test_vector_space[word] - univerdsal_vector_space[i][word])
            if chebyshev_distance > max_chebyshev_distance:
                max_chebyshev_distance = chebyshev_distance

    chebyshev_distance_dic[i] = max_chebyshev_distance
    i += 1

print("chebyshev dic is:")
print(chebyshev_distance_dic)
print(len(chebyshev_distance_dic))

sorted_chebyshevdist_dic = collections.OrderedDict(sorted(chebyshev_distance_dic.items(), key=operator.itemgetter(1)))
print("Sorted euclidean_distance_dic is:")
print(sorted_chebyshevdist_dic)
print(len(sorted_chebyshevdist_dic))


for k, v in sorted_chebyshevdist_dic.items():
    if k <= m:
        print("sport")
    elif m < k <= m+n:
        print("enter")
    else:
        print("eco")