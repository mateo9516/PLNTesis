import os
import sys 
import json
import nltk
from gensim.models import Word2Vec
from gensim.models import FastText
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize import sent_tokenize
import nltk.data
import csv
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

#Este se ejecuta de quinto

toktok = ToktokTokenizer()

#entries = os.scandir('./jsons') #escaneo la carpeta con los jsons
entries =  os.scandir('./corpus')

vocabulario = []

nube = ""

tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle') #necesario para que separe las unidades semanticas en español

row_count = 0    
with open('./normal.csv', 'rt',encoding="utf8") as f:
    row_count = sum(1 for row in f)
    #print(row_count)

f.close()

with open('./normal.csv', 'rt',encoding="utf8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    for i in range(1, row_count):
        #print(i)
        nube += mycsv[i][1]

sent = toktok.tokenize(nube)
all_sentences=nube
all_words = [toktok.tokenize(sent) for sent in sent_tokenize(all_sentences, language='spanish')]
model = FastText(all_sentences ,size=200, window = 6, min_count=3, workers=3)

# busco palabras similares, solo se puede con palabras que esten en el vocabulario

sim_words = model.wv.most_similar('afrocolombianas',topn=30) 

print(sim_words)  # imprimo las palabras similares, en nuestra prueba solo le atino a una, 
# la palabra "negra" 

def reduce_dimensions(model):
    num_dimensions = 2  # final num dimensions (2D, 3D, etc)

    # extract the words & their vectors, as numpy arrays
    vectors = np.asarray(model.wv.vectors)
    labels = np.asarray(model.wv.index2entity)  # fixed-width numpy strings

    # reduce using t-SNE
    tsne = TSNE(n_components=num_dimensions, random_state=0)
    vectors = tsne.fit_transform(vectors)

    x_vals = [v[0] for v in vectors]
    y_vals = [v[1] for v in vectors]
    return x_vals, y_vals, labels


x_vals, y_vals, labels = reduce_dimensions(model)

def plot_with_plotly(x_vals, y_vals, labels, plot_in_notebook=True):
    
    trace = go.Scatter(x=x_vals, y=y_vals, mode='text', text=labels)
    data = [trace]

    if plot_in_notebook:
        py.init_notebook_mode(connected=True)
        py.iplot(data, filename='word-embedding-plot')
    else:
        print("ploteando....")
        fig = go.Figure(data=data)
        py.plot(fig)


def plot_with_matplotlib(x_vals, y_vals, labels):
   

    random.seed(0)

    plt.figure(figsize=(12, 12))
    plt.scatter(x_vals, y_vals)

    #
    # Label randomly subsampled 25 data points
    #
    indices = list(range(len(labels)))
    selected_indices = random.sample(indices, 100)
    for i in selected_indices:
        plt.annotate(labels[i], (x_vals[i], y_vals[i]))

    plt.show()    

print("al try")

plot_with_matplotlib(x_vals, y_vals, labels)