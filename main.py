import csv
import pandas as pd
from cosine_module import cosineCal as Cc
import recomentdations as rec
from idf_tf_calculater import term_friquency as tf
from idf_tf_calculater import idf_calculate as idf
from idf_tf_calculater import tf_idf_calculate as tf_m_idf
# loading cleaned data
data = pd.read_csv('cleaned_data.csv')
# changing pandas dataframe into list
data = data.values.tolist()

# cleaned data matrix of id and description list
mat = []
for id, val in data:
    ls = val.split(' ')
    mat.append([id, ls])

# creating set of unique Words
uniqueWords = []
for id, val in mat:
    uniqueWords = set(val).union(uniqueWords)

# calculating term friquency matrix of the documents
tf_matrix = tf.tF_cal(mat, uniqueWords)
# claculating inverse document friquency
idf_dic = idf.calcIDF(tf_matrix, uniqueWords)
# calculating tf*idf
tf_idf_matrix = tf_m_idf.tf_idf_cal(tf_matrix, idf_dic)


# # converting list of dictionaries into list of list [[ids],[keys],[values of id1][values of id2],[values of id3].......[values of idn]]
temps = []
ids = []
for id, dic in tf_idf_matrix:
    temps.append(dic)
    ids.append(id)

new_tf_idf_matrix = [[key for key in temps[0].keys()], *
                     [list(idx.values())for idx in temps]]
new_tf_idf_matrix.insert(0, ids)

tf_m_idf_mat = new_tf_idf_matrix[2:]

# print(len(tf_m_idf_mat))
# calculating cocine similarity for the items
cosine_coefi_matrix = Cc.cosin_cal(ids, tf_m_idf_mat)
id_cof_matrix=[]

# converting list of id and dictionary into list of id and list
for id, dic in cosine_coefi_matrix:
    ls = [[k,v] for k,v in dic.items()]
    id_cof_matrix.append([id,ls])

# print(id_cof_matrix[10])  
recomended = rec.recomend(id_cof_matrix[10], 5)
print(recomended)
# # saving the final metriz into a csv file
# with open('new.txt', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(id_cof_matrix)
