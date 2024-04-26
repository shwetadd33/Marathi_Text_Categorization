from tfidf import *
from testnews import *
import collections
'''
print("***Vector space for sports category:***")
print(sport_vector_space)
print("length of sports vector space:")
print(len(sport_vector_space))
#print("\n\n")

print("***Vector space for entertainment category:***")
print(entertain_vector_space)
print("length of entertainment vector space:" , end= " ")
print(len(entertain_vector_space))
#print("\n\n")

print("***Vector space for economical affairs category:***")
print(economy_vector_space)
print("length of economical affairs vector space:")
print(len(economy_vector_space))
#print("\n\n")
'''

print("--------------------------------TESTING SECTION------------------------------------------------")
print("Test vector space:")
print(test_vector_space)
print(len(test_vector_space))

i=1
cosine_similarity_dic = {}
#euclidean_distance_dic[j] = {}

print ("*******************************************")
print(total_traindata)
while i <= total_traindata:
    dot_prod = 0
    test_norm = 0
    doc_norm = 0
    for word,frequency in test_vector_space.items():
        if word in univerdsal_vector_space[i].keys():
            dot_prod += univerdsal_vector_space[i][word] * test_vector_space[word]
            test_norm += pow(test_vector_space[word],2)
            doc_norm += pow(univerdsal_vector_space[i][word],2)
    sqrt_test_norm = math.sqrt(test_norm)
    sqrt_doc_norm = math.sqrt(doc_norm)
    dinominator_multi = sqrt_test_norm * sqrt_doc_norm
    if dinominator_multi == 0:
        cosine_similarity = -1
    else :
        cosine_similarity = dot_prod/(sqrt_test_norm * sqrt_doc_norm)
    cosine_similarity_dic[i] = cosine_similarity
    i += 1

print("cosine similarity dic is:")
print(cosine_similarity_dic)
print(len(cosine_similarity_dic))

sorted_cosinesim_dic = collections.OrderedDict(sorted(cosine_similarity_dic.items(), key=operator.itemgetter(1)))
print("Sorted euclidean_distance_dic is:")
print(sorted_cosinesim_dic)
print(len(sorted_cosinesim_dic))


for k, v in sorted_cosinesim_dic.items():
    if k <= m:
        print("sport")
    elif m < k <= m+n:
        print("enter")
    else:
        print("eco")


'''for keyvalue in euclidean_distance_dic:
    print("key value is")
    print(euclidean_distance_dic[keyvalue])'''

