# importing data from csv
import csv
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
import string
import pandas as pd
data = pd.read_csv('contentBased recomendation system\project\sample-data.csv')

# converting dataFrame object into list
data = data.values.tolist()

# convert the data into lowercase string
lowerCaseMatric = []
for key, val in data:
    ls = [val.lower()]
    lowerCaseMatric.append([key, ls])

# removing html tags from the data
    # i dont know what is happening here but got this code over "stack over flow" and appearently its working

TAG_RE = re.compile(r'<[^>]+>')
TagFreeMatrics = []
for key, desc in lowerCaseMatric:
    ls = []
    for word in desc:
        ls.append(TAG_RE.sub('', word))
    TagFreeMatrics.append([key, ls])

# removing punctuatins from tokenize docs
# define punctuation
punctuations = '''!()-[]{/};:'"\,<>./?@#$%^&*_~='''
pun_mat = []
for key, val in TagFreeMatrics:
    st = ""
    for char in val[0]:
        if char not in punctuations:
            st = st+char
    pun_mat.append([key, st])


# tokenizing the data
tokanizeMatrics = []
for key, val in pun_mat:
    ls = word_tokenize(val)
    tokanizeMatrics.append([key, ls])

# removing stop words
without_stop_words = []

for key, val in tokanizeMatrics:
    ls = []
    for word in val:
        if word not in stopwords.words('english'):
            ls.append(word)
    without_stop_words.append([key, ls])

# Lemmatizing the words
lamen_word = []
wlt = WordNetLemmatizer()
for key, val in without_stop_words:
    ls = []
    for word in val:
        ls.append(wlt.lemmatize(word))
    lamen_word.append([key, ls])

lamen_word.insert(0, ['id', ['description']])
# converting back the list of description into string
final_matrix = []
for key, val in lamen_word:
    final_matrix.append([key, " ".join(val)])

# saving the cleaned data into a csv file
with open('contentBased recomendation system\project\cleaned_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(final_matrix)
