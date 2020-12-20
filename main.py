import csv
import pandas as pd
from idf_tf_calculater import term_friquency as tf
from idf_tf_calculater import idf_calculate as idf
from idf_tf_calculater import tf_idf_calculate as tf_idf
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
tf_idf_matrix = tf_idf.tf_idf_cal(tf_matrix, idf_dic)



# saving the final metriz into a csv file
with open('tf_idf_matrix.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(tf_idf_matrix)


# print(pd.DataFrame(tf_idf_matrix))


