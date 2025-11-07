import numpy as np
import pandas as pd
import matplotlib as mpl

print(np.__version__)

'''Sirve para crear arrays'''
a= np.array([1,2,3,4,5])
print(a)

'''Array Bidimencional'''
b= np.array([{1,2,3},{1,2,3}])
print(b)

'''Array ZEROS(), crea arrays y los rellena de ceros'''
print("\n----------ZEROS-----------")
c= np.zeros(5)
print(c)

d= np.zeros([5,5])
print(d)

'''Array ONES(), crea arrays y los rellena de unos'''

print("\n----------ONES------------")
e= np.ones(4)
print(e)

f= np.ones([5,5])
print(f)

'''Recorrer Arrays'''

print("\n--------Recorrer--------")

g= np.arange(0,10)
print(g)

'''LINSPACE'''

print("\n--------Recorrer a la misma distancia todo--------")
h= np.linspace(0,2,4)
print(h)

'''Hace matrices EYE'''

print("\n--------EYE--------")
i= np.eye(5)
print(i)

'''RANDOM.RAND()'''

print("\n--------RANDOM.RAND()--------")
j= np.random.rand(5)
print(j)



'''---------------------------------------------PANDAS---------------------------------------------------'''

serie1 = pd.Series([1,2,3])
serie1.name="primeros"
print(serie1)

df1= pd.DataFrame({"columna1":[1,2,3,4,5], "columna2":["a","b","c","d","e"], "columna3":["?","!","¡","&","="]})
print(df1)

print("\n------------------------------DataFrame---------------------------------")

df2 = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
print(df2.head())

'''Muestra cuanto mide el DataFrame'''
print(df2.size);

'''Muestra la suma de todas las columnas y filas'''
print(df2.shape)

'''Es igual que head, pero muestra los 5 ultimos'''
print(df2.tail())

'''Muestra los indices o titulos de cada columna'''
print(df2.columns)

'''Muestra los identificadores de columna'''
print(df2.iloc)

'''Describe muestra estadisticas genericas'''
print(df2.describe)

print(df2["sepal_width"].value_counts())

'''Muestra el tipo de datos'''
print(df2.dtypes)

'''Muestra la memoria usada'''
print(df2.memory_usage().sum())

'''Para mostrar las columnas en el lado izquierdo'''
print(df2.T.head())

'''Para hacer que los datos se vean de forma decendente y ascendente'''
print(df1.sort_values("columna1"))
print(df1.sort_values("columna1", ascending=False))

'''Para tener una columna concreta'''
print(df1.iloc[[1,4],[1,2]])

print(df1[["columna1","columna3"]])

print(df1[df1["columna1"]>2])

print(df1.isna().sum())

#print(df1.columna1[3]=np.nan)

