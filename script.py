import spacy

def dictionary(list):
    list.sort()
    dict = {}
    for x in list:
        if x not in dict:
            dict.update({x:1})
        else:
            dict[x] += 1
    return dict

def addDicts(dict1, dict2):
    dict = dict1.copy()
    for x in dict2:
        if x not in dict:
            dict.update({x:dict2[x]})
        else:
            dict[x] += dict2[x]
    return dict

def lemmatized(list):
    lemmatized_list = []
    for token in list:
        lemmatized_list.append(token.lemma_)  
    return lemmatized_list

nlp = spacy.load("en_core_web_sm")
lemmatizer = nlp.get_pipe("lemmatizer")# 'rule'

f = open('2008/lvl1/cteni/1.txt','r')
text = f.read().replace('â€™','\'').replace('\n',' ')
text1 = dictionary(lemmatized(nlp(text)))
f.close()

f = open('2008/lvl1/cteni/2.txt','r')
text = f.read().replace('â€™','\'').replace('\n',' ')
text2 = dictionary(lemmatized(nlp(text)))
f.close()

vocabulary = addDicts(text1,text2)

print(vocabulary)