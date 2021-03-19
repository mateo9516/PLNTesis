import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set(style="white")

from gensim.models import Word2Vec, FastText

model = Word2Vec.load("C:/Users/Mateo/Documents/OCR/modelosAutogenerados/W2VSG/W2VSkipGram1473.model")

model.init_sims()

palabras = ["afrocolombianas","equivalencias","homologacion","rendimiento","asignatura","calificacion","reingreso","exencion","matricula","cancelacion"]

#obtengo palabras
aux_fila =[]
data = []

for palabra in palabras:
    for p in palabras:
        aux_fila.append(model.similarity(p,palabra))
    data.append(aux_fila)
    aux_fila=[]

print(data)

datos= pd.DataFrame(data, index = palabras, columns = palabras)
sns.heatmap(datos,cmap = sns.diverging_palette(250, 15, s = 75, l=40, n=16, as_cmap = True),
                vmax = 1.0, vmin = 0.0, 
                square = True, cbar = True)

plt.savefig('W2VSkipGram1473', format='png', dpi=300, bbox_inches='tight')
plt.show()