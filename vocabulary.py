from spacy import load
import io
from os import walk

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

def vocab_to_myVocab(vocab, myVocab):
    f = open(vocab,'r')
    text = f.read().split('\n')
    f.close()

    text.sort()

    f = open(myVocab,'w')
    for t in text:
        f.write(t + '\n')
    f.close()

def dict_to_vocab_file(dict, vocab_file):
    f = open(vocab_file, 'r')
    current = f.read().split('\n')
    f = open(vocab_file, 'w')
    for d in dict:
        if d not in current: 
            f.write(d + '\n')
            print(d)
    f.close()

def update_my_vocab(dict, vocab):
    f = open(vocab, 'r')
    current = f.read().split('\n')
    f.close()
    f = open(vocab, 'a')
    for d in dict:
        if d not in current:
            f.write(d + '\n')
            print(d)
    f.close()

# NEW FUNCTIONS
def lemmatized(list):
    lemmatized_list = []
    for token in list:
        lemmatized_list.append(token.lemma_)
    return lemmatized_list

def preprocess_list(list):
    stopwords = ['?',';','\n','\n\n','!','.',',',':']
    for item in list:
        if item in stopwords:
            list.remove(item)
        try:
            if int(item.encode('utf-8')) in range(33):
                list.remove(item)
            elif int(item.encode('utf-8')) in range(127,160):
                list.remove(item)
        except: pass
    return list

def update_vocab_with_text(vocab, text_file):
    with io.open(text_file,'r',encoding='utf8') as f:
        words = lemmatized(nlp(f.read()))
        words = preprocess_list(words)
        words = set(words)

    with io.open(vocab, 'r', encoding='utf8') as f:
        vocabulary = lemmatized(nlp(f.read()))

    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)

    vocabulary.sort()
    
    f = open(vocab, 'w')
    for word in vocabulary:
        if word != '\n':
            f.write(word + '\n')
    f.close()

def evaluate(text_file, vocab_file):
    know = 0
    unknow = 0
    with io.open(vocab_file,'r',encoding='utf8') as f:
        vocab = f.read().split('\n')

    with io.open(text_file,'r',encoding='utf8') as f:
        text = lemmatized(nlp(f.read()))

    for word in text:
        if word not in vocab:
            unknow += 1
        else:
            know += 1
    return know / (know + unknow)

def eval_folder(folder, vocab):
    f = []
    for (dirpath, dirnames, filenames) in walk(folder):
        f.extend(filenames)
        break
    for file in f:
        #
        percentage = round(evaluate(folder + '/' + file, vocab) * 100, 2)
        print(f'{percentage} % of {file}')
        
nlp = load("en_core_web_sm")
lemmatizer = nlp.get_pipe("lemmatizer")# 'rule'