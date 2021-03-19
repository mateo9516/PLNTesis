import sys
import os
import csv
import re
import json
import nltk
import numpy as np
from gensim.models import Word2Vec
from gensim.models import FastText
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize import sent_tokenize
import nltk.data
from nltk.corpus import stopwords
import tempfile

#############################################
#############################################

#CONSULTAS DE PRUEBA

#model = Word2Vec.load("word2vec.model")
#print(len(model.wv.vocab))
#model.build_vocab([["beneficios","admision","afro"]], update=True)
#model.train([["beneficios","admision","afro"]],total_examples=1,epochs=1)
#print(len(model.wv.vocab))
#annoy_index = AnnoyIndexer(model,100)

#############################################
#############################################

model = Word2Vec.load("C:/Users/Mateo/Documents/OCR/W2VCbow255.model")



print('Ingrese su consulta : ')
consulta = input()
entrada = []
consulta = consulta.split()


for x in consulta:
    if x in model.wv.vocab:
        entrada.append(x)

try:
        
    top = model.wv.most_similar(entrada,topn=30)

    lista_terminos = []
    lista_valores = []


    for palabra, valor in top:
        lista_terminos.append(palabra)
        lista_valores.append(valor)

    matriz = []
    with open('./Categorias.txt', 'rt',encoding='utf-8') as f:
        lineas = f.readlines()
        for linea in lineas:
            linea = linea.split('*')
            matriz.append(linea)

    aux=[]
    resoluciones = []
    valores =[]


    for a,b in matriz:
        aux=re.split(' |,',b)
        for i in range(len(lista_terminos)):
            if lista_terminos[i] in aux:
                elemento = matriz.index([a,b])
                if elemento not in resoluciones:
                    resoluciones.append(elemento)
                    valores.append(lista_valores[i])

    print(resoluciones)
    
    print('puede consultar las resoluciones: ')
    for i in range(len(resoluciones)):
        if valores[i] > 0.79:
            print(matriz[resoluciones[i]][0]," /// ",valores[i])
        
except:
    print("No se encontraron resultados")