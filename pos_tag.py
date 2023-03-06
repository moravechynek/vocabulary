import nltk
from nltk import word_tokenize

"""nltk.download('punkt')
nltk.download('average_percentron_tagger')
nltk.download('universal_tagset')"""

def rm_stopwords(list):
    stopwords = ['?',';','\n','\n\n','!','.',',',':']
    for item in list:
        if item[0] in stopwords:
            list.remove(item)
    return list

text = "This is one simple example. Yes, very simple example."
tokens = word_tokenize(text)

tags = nltk.pos_tag(tokens, tagset = 'universal')

tags = [ [t[0].lower(),t[1]] for t in tags]

tags = rm_stopwords(tags)

tags.sort()

f = open('myVocabulary.txt', 'w')
for pair in tags:
    f.write(f'{pair[0]} - {pair[1]}\n')
f.close()