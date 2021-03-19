from spellchecker import SpellChecker
import sys
import os
import csv
import re
import json
import nltk
from gensim.models import Word2Vec
from gensim.models import FastText
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize import sent_tokenize
import nltk.data
from nltk.corpus import stopwords
import tempfile
##### para mapear
from sklearn.decomposition import IncrementalPCA    # inital reduction
from sklearn.manifold import TSNE                   # final reduction
import numpy as np
from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
import random
import plotly.offline as py
import plotly.graph_objs as go
from IPython import get_ipython

texto = ""

entries = os.scandir('/Users/Mateo/Documents/OCR/corpus')
#wr = open('/Users/Mateo/Documents/OCR/prueba.txt',"w", encoding='utf-8') 

for entry in entries:
     textoName = entry.name
     f = open('/Users/Mateo/Documents/OCR/corpus/'+textoName,'r')
     for x in f:
        if(len(x)>1):
            texto+=x     

texto = texto.replace("\n"," ")
texto = texto.replace("-","")
texto = texto.replace("_","")
texto = texto.replace("°","")
texto = texto.replace(")","")
texto = texto.replace("(","")
texto = texto.replace("%","")
texto = texto.replace("—","")

def normalizar_texto(texto):
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@;:_-]°')
    BAD_SYMBOLS_RE = re.compile('[0-9]')
    INDIVIDUAL_LETTERS = re.compile('^[a-za-z]+')
    STOPWORDS = set(stopwords.words('spanish'))
    """
        texto : string 
        
        retorna: texto modificado
    """
    texto = texto.lower()
    texto = re.sub(REPLACE_BY_SPACE_RE,"",texto)
    texto = re.sub("[0-9]","",texto)
    texto = re.sub("\b[a-zA-Z]\b","",texto)
    aux=""
    words = texto.split()
    for r in words:
      if not r in STOPWORDS:
        aux+=r+" "
    text = aux.rstrip()
    return text

spell = SpellChecker(language='es')

arreglado = normalizar_texto(texto)

palabras = arreglado.split()

spell.word_frequency.load_words(['homologacion'])

misspelled = spell.unknown(palabras)
print(len(palabras))
print(len(misspelled))

for word in misspelled:
    # Get the one `most likely` answer
    # Get a list of `likely` options
    arreglado = arreglado.replace(word,spell.correction(word))

tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle') #necesario para que separe las unidades semanticas en español

sent = toktok.tokenize(arreglado)
all_sentences=sent_tokenize(arreglado)

for i in range(len(all_sentences)):
    all_sentences[i] = re.sub("\W+"," ", all_sentences[i])
    all_sentences[i] = re.sub(r"\W*\b\w{1,3}\b","",all_sentences[i])

print(len(all_sentences))

all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
 # con esto separo todas las palabras de las supuestas oraciones
model = Word2Vec(all_words, size=200, window = 7, min_count=4, workers=3,sg=1) # este es el modelo del word2vec

model.save("word2vecWithSpell.model")

sim_words = model.wv.most_similar('afrocolombianas',topn=30)

print(sim_words)