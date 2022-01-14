import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
d=pd.read_csv("iris.csv")
print(d)
print(d.shape)
print(d.describe())
a=d[:]['species']
b=a.count()
print(b)
c1=0
c2=0
c3=0
for i in range(b):
    if a[i]=='setosa':
        c1=c1+1
    if a[i]=='versicolor':
        c2=c2+1
    if a[i]=='virginica':
        c3=c3+1
print('setosa',c1,'\nversicolor',c2,'\nvirginica',c3)
print(d.groupby('species'))
#for i in range(b):
#plt.hist(d.sepal_length[i])
#plt.show()
'''
d.hist(bins=10)
plt.xlabel(['species'])
plt.show()'''
pd.plotting.scatter_matrix()
