# importing data from csv
import csv
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
import string
import pandas as pd
data = pd.read_csv('sample-data.csv')

# converting dataFrame object into list
data = data.values.tolist()

# convert the data into lowercase string
lowerCaseMatric = []
for id, val in data:
    ls = [val.lower()]
    lowerCaseMatric.append([id, ls])

# removing html tags from the data
    # i dont know what is happening here but got this code over "stack over flow" and appearently its working

TAG_RE = re.compile(r'<[^>]+>')
TagFreeMatrics = []
for id, desc in lowerCaseMatric:
    ls = []
    for word in desc:
        ls.append(TAG_RE.sub('', word))
    TagFreeMatrics.append([id, ls])

# removing punctuatins from tokenize docs
# define punctuation
punctuations = '''!()-[]{/};:'"\,<>./?@#$%^&*_~='''
pun_mat = []
for id, val in TagFreeMatrics:
    st = ""
    for char in val[0]:
        if char not in punctuations:
            st = st+char
    pun_mat.append([id, st])


# tokenizing the data
tokanizeMatrics = []
for id, val in pun_mat:
    ls = word_tokenize(val)
    tokanizeMatrics.append([id, ls])

# removing stop words
without_stop_words = []

for id, val in tokanizeMatrics:
    ls = []
    for word in val:
        if word not in stopwords.words('english'):
            ls.append(word)
    without_stop_words.append([id, ls])

# Lemmatizing the words
lamen_word = []
wlt = WordNetLemmatizer()
for id, val in without_stop_words:
    ls = []
    for word in val:
        ls.append(wlt.lemmatize(word))
    lamen_word.append([id, ls])

lamen_word.insert(0, ['id', ['description']])
# converting back the list of description into string
final_matrix = []
for id, val in lamen_word:
    final_matrix.append([id, " ".join(val)])

# saving the cleaned data into a csv file
with open('cleaned_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(final_matrix)
