import nltk
from nltk import word_tokenize

nltk.download('punkt')
nltk.download('average_percentron_tagger')
nltk.download('universal_tagset')

text = "This is one simple example."
tokens = word_tokenize(text)
tokens = [t.lower() for t in tokens]
tokens.sort()

tags = nltk.pos_tag(tokens, tagset = 'universal')

f = open('myVocabulary.txt', 'w')
for pair in tags:
    f.write(f'{pair[0]} - {pair[1]}')
f.close()