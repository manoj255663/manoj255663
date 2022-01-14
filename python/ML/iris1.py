import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import model_selection 
d=pd.read_csv("iris.csv")
#print(d)
print(d.shape)
print(d.describe())
print(d.groupby('species'))
'''
setosa=0
versicolor=0
virginica=0
for a in range(0,150):
    if(d.species[a]=="virginica"):
        virginica=virginica+1
    elif(d.species[a]=="versicolor"):
        versicolor=versicolor+1
    elif(d.species[a]=="setosa"):
        setosa=setosa+1
print("setosa :",setosa)
print("virginica :",virginica)
print("versicolor :",versicolor)
	'''			    						    			    
#for a in range(0,150):
'''plt.hist(d.sepal_length)
plt.hist(d.sepal_width)
plt.hist(d.petal_length)
plt.hist(d.petal_width)'''
#d.hist()
#plt.show()
#print(scatter_matrix(species))
print(pd.plotting.scatter_matrix(species))
